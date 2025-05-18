import 'dotenv/config'
import fs from "fs/promises"
import path from "path"
import axios from "axios"

const PINATA_JWT = process.env.PINATA_JWT
if (!PINATA_JWT) throw new Error("PINATA_JWT is not defined in env")

const rootDir = "public"

async function walk(dir, base = "") {
  const entries = await fs.readdir(dir, { withFileTypes: true })
  const files = []
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name)
    const relPath = path.join(base, entry.name)
    if (entry.isDirectory()) {
      files.push(...(await walk(fullPath, relPath)))
    } else {
      const content = await fs.readFile(fullPath, "utf8")
      files.push({
        name: path.basename(relPath),
        path: relPath,
        content,
      })
    }
  }
  return files
}

const files = await walk(rootDir)

const res = await axios.post(
  "https://api.pinata.cloud/v3/pins",
  {
    metadata: { name: "QuartzSite" },
    content: files,
  },
  {
    headers: {
      Authorization: `Bearer ${PINATA_JWT}`,
      "Content-Type": "application/json",
    },
  }
)

console.log("✅ Uploaded to Pinata")
console.log("🧬 CID:", res.data.requestid)
console.log("🌐 Gateway: https://gateway.pinata.cloud/ipfs/" + res.data.requestid)
