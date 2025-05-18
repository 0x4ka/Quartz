import { PinataSDK } from "pinata"
import fs from "fs/promises"
import path from "path"
import dotenv from "dotenv"

dotenv.config()

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT,
})

const publicDir = "./public"

// 再帰的に File[] を構成する
async function collectFiles(dir, base = "") {
  const entries = await fs.readdir(dir, { withFileTypes: true })
  const files = []

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name)
    const relPath = path.join(base, entry.name)

    if (entry.isDirectory()) {
      const subfiles = await collectFiles(fullPath, relPath)
      files.push(...subfiles)
    } else {
      const content = await fs.readFile(fullPath)
      const file = new File([content], relPath) // ← ここで File オブジェクトを構成
      files.push(file)
    }
  }

  return files
}

const fileArray = await collectFiles(publicDir)

const upload = await pinata.upload.public
  .fileArray(fileArray)
  .name("0xhid3-quartz")

console.log("✅ Uploaded!")
console.log("🧬 CID:", upload.cid)
console.log("🌐 Gateway:", `https://gateway.pinata.cloud/ipfs/${upload.cid}`)