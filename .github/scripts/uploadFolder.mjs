import { PinataSDK } from "pinata"
import fs from "fs/promises"
import path from "path"
import { Blob } from "buffer"
import fileFromBuffer from "web3-file"
import dotenv from "dotenv"

dotenv.config()

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT,
})

const publicDir = "./public"

// 再帰的にファイルを集めて File[] に変換
async function collectFiles(dir, base = "") {
  const entries = await fs.readdir(dir, { withFileTypes: true })
  const files = []

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name)
    const relativePath = path.join(base, entry.name)

    if (entry.isDirectory()) {
      const subfiles = await collectFiles(fullPath, relativePath)
      files.push(...subfiles)
    } else {
      const content = await fs.readFile(fullPath)
      const file = await fileFromBuffer(content, relativePath)
      files.push(file)
    }
  }

  return files
}

const fileArray = await collectFiles(publicDir)

const upload = await pinata.upload.public
  .fileArray(fileArray)
  .name("QuartzSite")
  .key
