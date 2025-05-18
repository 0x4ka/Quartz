import { PinataFDK } from "pinata-sdk";
import path from "path";

const pinata = new PinataFDK({
  pinataJwt: process.env.PINATA_JWT,
});

const folderPath = path.resolve("public");

const upload = await pinata.upload.directory(folderPath);

console.log("✅ CID:", upload.cid);
console.log("🌐 Gateway:", `https://gateway.pinata.cloud/ipfs/${upload.cid}`);
