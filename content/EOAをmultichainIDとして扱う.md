---
title: "EOAをmultichainIDとして扱う"
date: 2024-03-30T10:05:38.000+09:00
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

