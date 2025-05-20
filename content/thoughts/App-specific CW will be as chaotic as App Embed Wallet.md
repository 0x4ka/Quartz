---
title: 'App-specific CW will be as chaotic as App Embed Wallet'
date: 2024-03-30T17:06:49.000+09:00
tags: 
---

#Wallet

App Embed Wallet is a [[wallet]] hidden in the app I/F like STEPN etc.
These are generally called dApp Wallets
App Embed Wallet はSTEPNなどのようにアプリI/Fに隠蔽されたウォレットのこと
これらは総じて [[dApp Wallet]] と呼ぶ

- A world where each application generates its own [[CW]] with its own interface and logic is chaotic
- アプリケーション毎に独自のインターフェースやロジックを持つCWが生成される世界はカオス
    - cons
        - if there are 10 dapps, user have to deploy 10 wallet for each applications.
        - ユーザーは、利用するアプリケーションが10個あるだけで、10個のwalletを管理する必要がある
        - Switching those contract wallet on frontend interface is mandantry (Abstract UX by UI is possible but it's not essencial.
        - インターフェース上での切り替えが必須（UIで抽象化することも可能だけど本質的ではない）
    - pros
        - Enclose users in the application
        - アプリケーションにユーザーを囲い込むことができる
        - Ability to develop products independent of CW Provider's implementation roadmap
        - CW Provider の実装ロードマップに依存しないでプロダクトを開発できる

If the cost of transferring assets were as close to zero as possible, could a dApp Wallet be a prerequisite?
仮に資産の移転コストが限りなく0に近づいた場合、dApp Wallet が前提になりえるか?
- gas cost
- bridge cost
- cognitive load 認知負荷
    - Cognitive load due to the distributed presence of wallets for each application
    - ウォレットがアプリケーション毎に分散して存在することによる認知負荷
        - An aggregator that integrates and displays wallets is essential
        - wallet を統合して表示するアグリゲータが不可欠
            - There is also the technical question of how to perform the wallet operation
            - wallet の操作をどう実行するかという技術的な問いも存在する
- Security risk
    - The frequency with which users move assets from wallet to wallet correlates to the level of vulnerability
    - ユーザーがwallet から wallet に資産を動かす頻度は脆弱性のレベルに相関する

fyi:
- [[Personal wallet vs Embed wallet]]
