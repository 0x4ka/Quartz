require("dotenv").config()
const fs = require("fs");
const path = require("path");
const axios = require("axios");
const FormData = require("form-data");

const PINATA_JWT = process.env.PINATA_JWT;
if (!PINATA_JWT) throw new Error("PINATA_JWT is not defined");

const PUBLIC_DIR = "./public";

function getAllFiles(dirPath, arrayOfFiles = [], base = "") {
  const files = fs.readdirSync(dirPath);
  files.forEach((file) => {
    const fullPath = path.join(dirPath, file);
    const relativePath = path.join(base, file);
    if (fs.statSync(fullPath).isDirectory()) {
      getAllFiles(fullPath, arrayOfFiles, relativePath);
    } else {
      arrayOfFiles.push({ path: fullPath, relativePath });
    }
  });
  return arrayOfFiles;
}

async function uploadToPinata() {
  const form = new FormData();
  const files = getAllFiles(PUBLIC_DIR);

  files.forEach(({ path: filePath, relativePath }) => {
    form.append("file", fs.createReadStream(filePath), { filepath: relativePath });
  });

  const res = await axios.post("https://api.pinata.cloud/pinning/pinFileToIPFS", form, {
    headers: {
      Authorization: `Bearer ${PINATA_JWT}`,
      ...form.getHeaders(),
    },
    maxBodyLength: Infinity,
  });

  console.log("✅ Upload successful!");
  console.log("🧬 CID:", res.data.IpfsHash);
  console.log("🌐 https://gateway.pinata.cloud/ipfs/" + res.data.IpfsHash);
}

uploadToPinata().catch(console.error);
