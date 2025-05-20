---
title: "safe の module は権限分離を主眼としている"
date: "1970-01-20T11:56:02.826Z"
tags:
  
---

#wallet #WalletContract

- Safeは2B
    - 組織内で1つのウォレットを共有（tresuary）し、multisigで承認を行うことを前提に設計されている
    - toCは、[[Biconomy Smart Contract Wallet]]や[[argent]]が担う

SafeはDAO等組織のトレジャリー管理向けなので、組織のOwnerが設計したModuleとその他SignerによるTxを検証するGuardをあらかじめ設定した上で運用される思想
- なので、Moduleの付け替えというのは、Ownerだけが行う想定
    - その他signerはGuardによってこの操作を実現できない
    - moduleによる権限分離がコアなコンセプト

- 統治者としてのGuard
- Moduleは機能的アップグレードの要件を満たすためのパターン設計？

- 下記動画の内容からも思想を読み取れる
[https://www.youtube.com/watch?app=desktop&v=vpnHR0rsMl0](https://www.youtube.com/watch?app=desktop&v=vpnHR0rsMl0)

