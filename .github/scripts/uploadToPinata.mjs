import { PinataFDK } from "pinata-sdk";
import path from "path";
import "dotenv/config";

const pinata = new PinataFDK({
  pinataJwt: process.env.PINATA_JWT,
});

const folderPath = path.resolve("public");

console.log("📦 Uploading folder:", folderPath);

const upload = await pinata.upload.directory(folderPath);

console.log("✅ Uploaded to Pinata!");
console.log("🧬 CID:", upload.cid);
console.log("🌐 Gateway: https://gateway.pinata.cloud/ipfs/" + upload.cid);
