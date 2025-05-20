---
title: "multichainIDはチェーンに依存すべきではない"
date: 2024-03-30T10:32:35.000+09:00
tags: 
---

#MultichainID
create2によるマルチチェーン間のアドレスの一致を期待することは非現実的である
- ブロックチェーンのストレージの使用によって左右される
    - [https://forum.safe.global/t/how-can-a-safe-hold-asset-on-multiple-chains/2242/26](https://forum.safe.global/t/how-can-a-safe-hold-asset-on-multiple-chains/2242/26)
- EVM系に閉じる
- すでに指定のアドレスがデプロイされていないことを保障しなければならない

[https://forum.safe.global/t/how-can-a-safe-hold-asset-on-multiple-chains/2242/8](https://forum.safe.global/t/how-can-a-safe-hold-asset-on-multiple-chains/2242/8)
