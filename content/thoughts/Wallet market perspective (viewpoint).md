---
title: "Wallet market perspective (viewpoint)"
date: 2023-04-28T14:23:05.000+09:00
tags: 
---

#wallet

<img src='https://scrapbox.io/api/pages/0xhid3-private/public/icon' alt='public.icon' height="19.5"/>

下記記事を参考にウォレット市場の要点をメモってる
source: [Crypto Research, Data, and Tools | Messari](https://messari.io/report/crypto-wallets-landscape-and-strategies?referrer=pro-research)

> ウォレット市場は、キャズムの向こう側にいるユーザーにサービスを提供するためのさまざまなソリューションの開発において、大きな進歩を遂げました。その中でも、マルチパーティコンピュテーション（MPC）とスマートコントラクト（SC）ウォレットは、物語を支配してきた。
- 2022年8月「Applying Multiparty Computation to the World of Blockchains」
- 2022年11月「[Seedless Self-Custody: On MPC and Smart Contract Wallets | 1kxnetwork](https://medium.com/1kxnetwork/wallets-91c7c3457578)
- 2023年3月「[Crypto Research, Data, and Tools | Messari](https://messari.io/report/a-path-towards-account-abstraction-with-erc-4337?referrer=all-research)
- 等々、ウォレット市場における話題は、MPCやSCウォレットに関する内容が支配的だったらしい

- ウォレットはトップに立つことで勝てるが、現状のアプリケーションを今後利用するであろう数百万人が利用できるとは思えない
    - ウォレット単独に実用性がなく、現状は高いリテラシーとリスク許容度を持つユーザーが高度に活用しているにすぎない
    - metamaskは、2022年12月から執筆現在までの4ヶ月間の間だけで $20M の収益を獲得している
        - ![image](https://scrapbox.io/files/644bb78537eb4f001b598aee.png)
    - Swapperは32万人ほど
        - 一人当たり累計62ドルのスワップ手数料を支払っているということになる
        - 手数料は0.875% [source](https://consensys.net/blog/metamask/the-most-trusted-way-to-buy-store-and-swap-tokens-just-went-mobile/)
        - [https://dune.com/Marcov/metamask-swap](https://dune.com/Marcov/metamask-swap)
- 現状のウォレットが抱えている課題
    - セキュリティの欠如
    - 使いにくいUX
    - ユーザーが想起しやすい実用性

- Wallet Solutionは4つのコンテキストへ整理
    - 鍵管理
        - account creation
        - transaction & message signing
    - ブロックチェーン接続性
        - RPC connectivity
    - ユーザーインターフェース
        - Browser extention
        - mobile app
        - popup
    - アプリケーションロジック
        - smart contract account
        - session keys
        - time-based permissions
![image](https://scrapbox.io/files/644bb3eb169760001cdce07a.png)

- 階層型決定論の脆弱性
    - 鍵管理：Master private key の流出はその先全ての秘密鍵流出を意味する
    - 接続性：RPCサーバを通して特別なことなく接続可能
    - UI：署名の要求が多くユーザー体験を阻害する
    - アプリケーションロジック：プログラムによるビジネスロジックの構築ができない（フロントを用いて組み合わせることは可能）
- Smart Contract Wallet
    - 鍵管理：マルチシグの利用は注意が必要であるが有用である
    - 接続性：EOAを必要とする。Bundlerを用いた簡略化が議論されているが [BEV](https://scrt.network/blog/erc-4337-and-mpc-friends-or-foes) の設計が重要そう
    - UI：reference to Argent and Safe
    - アプリケーションロジック：ユースケースに関する記事を参照。このデザイン空間はめっちゃでかい
        - [ERC-4337 and MPC: Friends or Foes? | Secret Network Blog](https://scrt.network/blog/erc-4337-and-mpc-friends-or-foes)
- MPC/TSSウォレット
    - 鍵管理：マルチシグと同様に秘密鍵という単一障害点を排除
    - 接続性：MPCはチェーンにとらわれることがない（EOAだもんね）しかしMPCそのものへのトラストが発生していることには注意する必要がある
    - UI：coinbaseのWaaSのようにカウンターパーティを一元化する場合と、Lit Actionのような分散型カウンターパーティの模索が行われている
    - アプリケーションロジック：MPCも実態はEOAであるためプログラムによるビジネスロジックの記述はできないが、オフチェーンでの任意のロジック→秘密鍵復元→署名のような仕組みを作ることは可能（トラストが発生する）

競合市場のマッピング
![image](https://scrapbox.io/files/644bb3eb169760001cdce07a.png) ![image](https://scrapbox.io/files/644bb32b507403001b33a7b3.png)
- 観点
    - セキュリティ
    - アクセシビリティ
    - スペシャリティ
    - ビジネスフォーカス
