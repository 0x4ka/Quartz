import fs from 'fs';
import path from 'path';
import FormData from 'form-data';
import got from 'got';
import dotenv from 'dotenv';

dotenv.config();

const PINATA_JWT = process.env.PINATA_JWT; // 環境変数からJWTを取得
const PUBLIC_DIR = path.join(process.cwd(), 'public');

async function uploadFolder() {
  const form = new FormData();

  // publicディレクトリ内のファイルを再帰的に読み込む
  function readFilesRecursively(dir, base = '') {
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
      const fullPath = path.join(dir, entry.name);
      const relativePath = path.join(base, entry.name);
      if (entry.isDirectory()) {
        readFilesRecursively(fullPath, relativePath);
      } else {
        form.append('file', fs.createReadStream(fullPath), {
          filepath: relativePath, // 相対パスを指定
        });
      }
    }
  }

  readFilesRecursively(PUBLIC_DIR);

  // wrapWithDirectoryオプションを設定
  form.append('pinataOptions', JSON.stringify({ wrapWithDirectory: true }));

  try {
    const response = await got.post('https://api.pinata.cloud/pinning/pinFileToIPFS', {
      body: form,
      headers: {
        Authorization: `Bearer ${PINATA_JWT}`,
        ...form.getHeaders(),
      },
    }).json();

    console.log('✅ アップロード成功:', response);
  } catch (error) {
    console.error('❌ アップロード失敗:', error.response?.body || error.message);
  }
}

uploadFolder();
