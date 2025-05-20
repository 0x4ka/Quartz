---
title: "memo"
date: 1970-01-20T11:24:07.201Z
tags: 
---

wallet meets dappは手段
ビジョンはNFTの最適分配
- how to realize パート
    - contract wallet and Argent Modules
    - streaming payment

Team
- what we are
- ETH india でコントラクトウォレットの高い専門性
- ETH tokyo でレンタルプロトタイプの実装済み

## Realize
- make nft market more friendly
- NFTの流動性拡大と最適分配を達成する
    - 流動性の最大化と最適分配は異なる
    - 流動性は一部高いが、最適な分配ではない
## Problem
- 求めている人へ届きにくい市場（価格的な参入障壁）
    - 資本主義的には高価格帯で取引される市場があればそれは正義⇔所有の概念を段階的にすることでこの前提を変えられるはず
        - 売却価格は高価格帯に留まるが、段階的な所有の取引は中低価格帯に降ってくるかも
- ブロックチェーン上では売り買いすることしかできない
    - 所有するなら購入するしかない↔︎非所有になるためには売却するしかない
## Solution
- We define gradual ownership by streaming NFT and Module based  contract wallet.
    - 所有と非所有の間を選べるようにする
    - レンタルでもあり分割払いでもある
## How it works
- ユーザーはNFTのストリーミングを開始すると毎秒トークンを支払う
- 売手（貸手）が指定した金額に達するとトークンの所有権が完全に移転する
    - これは非所有の状態から所有の状態まで徐々に変化することを実現している
- 購入する場合：
    - 売り手が指定する数量を支払うことで購入できる
- レンタルの場合：
    - 途中で支払いを中断すれば所有権を購入せずに一時的な利用を実現できる
## Benefit Why Gradual Ownership?
- 購入前にトライアルを体験する
    - ユーザーは購入するか検討するために一時的にレンタルすることが可能です
- 分割支払いで購入する
    - ユーザーは一括ではなく分割して支払いすることが可能です
- 資産を安全に保ちながら資金効率高く売却する
    - 売り手（あるいは貸手）は、売却の機会に加えて売却に至るまでの勾配による金利収益を獲得できます
## Current NFT rental requires technical supports on App
![image](https://scrapbox.io/files/644ad1b97ac9ce001b252bdf.png)



CWのデプロイ数と取引数の推移、成長率
- Safeのストア学
    - [https://dune.com/queries/1012/1699](https://dune.com/queries/1012/1699)
- Argent
    - [https://dune.com/queries/1612/2789](https://dune.com/queries/1612/2789)

NFT市場の停滞は、興味の喪失？いや、仮に手の届く価格なら興味本位でコンテンツを体験したい人はいるかも知れない。
- しかしホルダーは手放そうとしない
    - なぜなら彼らは次のバブルを期待しているから
    - 手放さずに金利を得られるなら？
        - その価格競争は新たな均衡価格の形成に寄与するだろう


所有の変化をBinary→Gradualに
toggle→slider（days）
it's time to move gradually

do you want to buy it?
you don't need buy it.
pay as you use then get gradually.

![image](https://scrapbox.io/files/644acffdaf095e001c6e4643.png)