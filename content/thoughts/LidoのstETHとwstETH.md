---
title: "LidoのstETHとwstETH"
date: June 5, 2023 (TZ: UTC+9)
tags: 
---

#LSD

source: [stETH, wstETH で安定 ETH ステーキング運用したいメモ](https://zenn.dev/syoyo/articles/0667f7deb8a040)

- stETHはリベースされるトークン
    - ETH:stETHは基本的に1:1
    - たまにdepegする
    - >  1.0 ETH -> 1 stETH
    - >   (一年くらいまつ)
    - >   残高が 1.05 stETH になる
    - >   1.05 stETH -> 1.05 stETH
- Dune
    - [https://dune.com/LidoAnalytical/lido-execution-layer-rewards](https://dune.com/LidoAnalytical/lido-execution-layer-rewards)

- 用途
    - AAVEに預ける
    - ステーキング報酬を得つつ、USDC借入が可能
    - AAVE では, 現状は stETH 自体を借りる需要はほとんどないため, stETH を deposit することによる AAVE からの利息はほぼゼロです
    - 最近はETH Mainnetのガスコストが高すぎるため、PolygonやL2での利用を促進するべくwstETHの利用を推進している
        - > ユーザーは、stETHをイーサリアムメインネットのLidoで包装資産「wstETH（Wrapped stETH）」に変換してから、AribitrumとOptimismの公式ブリッジでwstETHを移送できる。 by [LidoのstETH、イーサリアムL2への展開を開始](https://coinpost.jp/?p=395155)
        - ETHステーキング報酬はwstETHをstETHに戻した時に反映
        - 対応プラットフォーム
            - Beethoven X
            - Balancer
            - Curve Finance
            - Kyber NetworkVelodrome

- リベースについて
    - source: [Defiを理解しようシリーズ 第4回：レバレッジの悪魔 ～stETHレバレッジステーキング～｜dK](https://note.com/dkcrypto1/n/n2c9d07c2c8a6#4db42adf-a79e-49ce-afe1-284597efbfa8)
    - stETHは、ERC20のトークンであり、保有しているだけでAmountが増加していきます
        - `balanceOf(account) = shares[account] * totalPooledEther / totalShares`
    - しかしこの仕組みを一般的なプロトコルは対応していない
        - > stETHをAmount Xで預入れ、その代わりにcTokenを同量受け取ったとします。
        - >  この際のstETHの所有者はプロトコルとなり、cTokenと同量のstETHをClaimできます。
        - >  しかし預け入れられたstETHはリベースされていきますが、cTokenはリベースされません。つまり常にXのstETHしか保有できないことになります。
    - これを解決するのが、wstETH
        - wstETHはamountが増加するのではなく、priceが増加する

