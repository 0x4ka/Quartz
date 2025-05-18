require("dotenv").config() // 任意。ローカルでは.envから読む用

const axios = require("axios")
const FormData = require("form-data")
const fs = require("fs")
const path = require("path")

const PINATA_JWT = process.env.PINATA_JWT
if (!PINATA_JWT) {
  throw new Error("PINATA_JWT is not defined in env");
}
const DIRECTORY_TO_UPLOAD = "./public"

async function uploadFolderToPinata(dirPath) {
  const form = new FormData()

  function addFilesToForm(currentPath, relativePath = "") {
    const entries = fs.readdirSync(currentPath, { withFileTypes: true })

    entries.forEach((entry) => {
      const fullPath = path.join(currentPath, entry.name)
      const entryRelativePath = path.join(relativePath, entry.name)

      if (entry.isDirectory()) {
        addFilesToForm(fullPath, entryRelativePath)
      } else {
        form.append("file", fs.createReadStream(fullPath), {
          filepath: entryRelativePath,
        })
      }
    })
  }

  addFilesToForm(dirPath)

  const metadata = JSON.stringify({
    name: "QuartzSite",
  })
  const options = JSON.stringify({
    cidVersion: 1,
  })

  form.append("pinataMetadata", metadata)
  form.append("pinataOptions", options)

  const res = await axios.post("https://api.pinata.cloud/pinning/pinFileToIPFS", form, {
    maxContentLength: Infinity,
    maxBodyLength: Infinity,
    headers: {
      ...form.getHeaders(),
      Authorization: `Bearer ${PINATA_JWT}`,
    },
  })

  console.log("✅ Uploaded to Pinata!")
  console.log("🌐 Gateway URL:", `https://gateway.pinata.cloud/ipfs/${res.data.IpfsHash}`)
  console.log("🧬 CID:", res.data.IpfsHash)
}

uploadFolderToPinata(DIRECTORY_TO_UPLOAD).catch(console.error)
