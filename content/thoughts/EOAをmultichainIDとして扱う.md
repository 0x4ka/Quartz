---
title: "EOAをmultichainIDとして扱う"
date: March 30, 2024
tags: 
---

#MultichainID #WalletContract #wallet

ref: [https://ethereum-magicians.org/t/chain-specific-addresses/6449](https://ethereum-magicians.org/t/chain-specific-addresses/6449)


複数のコントラクトウォレットに対して、単一のeoaが操作権限を持ち
ソーシャルリカバリーの余地を与える
eoaはIDとして機能する

EOAの作成をソーシャルアカウントで実装
- key management: MPC
EOA→ENS subdomainの提供
- プロパティに各チェーンのAAウォレットを紐付け（[[MultichainID]]）

