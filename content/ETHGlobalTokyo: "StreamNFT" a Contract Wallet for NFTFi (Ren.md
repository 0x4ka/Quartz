---
title: "ETHGlobalTokyo: 'StreamNFT' a Contract Wallet for NFTFi (Rental)"
date: 2023-05-04T10:17:52.000+09:00
tags: 
---

#wallet #WalletContract #ETHGlobalTokyo

[Streaming NFT with wallet | ETHGlobal](https://ethglobal.com/showcase/streaming-nft-with-wallet-n559o)
[StreamNFT_demo.mp4 - Google Drive](https://drive.google.com/file/d/1iwAIBYtcjoWWM1MU1FF_S7kxeecEVVlX/view)
[Pitch Deck](https://docs.google.com/presentation/d/17-PlgmMdIo2TNwGLHq43wmMKYwoYNWAHeNIu6byV6hY/edit?usp=sharing)



## Abst.
A Wallet with a NFT rental function that allows you to rent when you need it and lend it when you don't need it. Rentals can be from just 1 second to indefinitely and Renter just pay for while using.
- Stream NFT
    - don't need to own, just stream.
    - Pay as you use
    - NFTを所有することなく使用した分だけ支払うストリーミングサービス
- Smart Contract Walletを使うことで、WrapやERC4907ではないオリジナルなNFTを配信される
- NFTを購入するというリスクを追うことなく、NFTに付帯するコンテンツを体験できる
    - 今回は、「ウォレットにNFTを置いておくだけで収益を得られる」という訴求ポイントは保留する
        - あくまで借りる人が、手軽に、使った分だけ支払いを負担するというところが重要

### Description
- このプロジェクトは、コントラクトウォレットを利用することで、ユーザーがNFTを使いたい時にレンタルし、必要ない時に、手軽に貸し出せるようにしてます。ビデオを購入せずストリーミング配信で映像を見るように、NFTを所有することなくコンテンツの体験を提供します。

### how it build
- このプロジェクトは、スマートコントラクトにLit Protocolを組み合わせることでトランザクションのたびに発生する署名操作を可能な限り排除しています。また、レンタル料金の支払いにSuperfluidを利用することでレンタル期限を決めずに借りている間だけ支払いを実行しています。返却し忘れると永遠に支払続けられてしまうため、Lit Actionを組み合わせることで、ユーザーがNFTの返却日時を予約出来るようにしています。貸出されたNFTや所有しているNFTのメタデータを扱うフロントエンド・バックエンドではAirstackを活用しています。

## Problem
私たちは、NFT市場へ新たなユーザーをオンボーディングするために「NFTの所有」の再定義を試みている。
- NFTを所有することはダウンサイドシナリオに対するリスクを背負うこととイコールになっている。そのため、NFTレンタルというソリューション（ERC4907方式やRegistry方式）が提供され始めているが、dApp側に技術対応を求めてしまう。
    - ⇄ 私たちは、Smart Contract Walletを使うことで、dApp側の技術対応なしにオリジナルなNFTのレンタルを実現
    - ダウンサイドシナリオ
        - 過去1年間での減少率
        - 7日間での減少率
        - めっちゃボラタイル（持つこと自体がリスクになる）
- 使ったことのないNFTをいつまで借りるべきか判断するのは難しいから大体1日で借りる。借り続けたい時は毎回txしないといけない
    - ⇄ あらかじめ日数を決める形式では、借りる瞬間に取引が終了するため借り直す必要がある→ガス効率悪い、借り続けることに対する評価がない
- また、レンタルが長く借りることのインセンティブがない（長く借りたからといって本来のNFTが安くなるわけでも、レンタル料が安くなるわけでもない）
    - ⇄

## Solution
### Don't need to own, just stream.
- Pay as you use
    - Streaming
- Contract Wallet
    - Whole NFTs are supported

## Demo
- Streaming flow
    - Wallet を作成する（Lit ProtocolでoAuthを使ってログイン?）
    - レンタル用にトークンをSwapする（あるいは最初から預けておく・署名はAA / Lit protocol で省略される）
    - 「レンタル」タブを開いて、借りたいNFTを選択する
    - NFT詳細画面で「Stream now」をタップする（署名はAA / Lit protocol で省略される）
    - （SuperfluidのStreamが開始する）
    - NFT詳細画面で「Stop now」をタップする（署名はAA / Lit protocol で省略される）
    - （SuperfluidのStreamが終了する）
> Lend flow（**Figmaの画面だけ作ります）
>  	Wallet を作成する（Lit ProtocolでoAuthを使ってログイン?）
>  	WalletにNFTをdepositする
>  	「List」タブを開いて、借したいNFTを選択する
>  	NFT詳細画面で「List now」をタップする
>  	貸出条件を設定する（毎分○eth）
>  	StreamされるとウォレットにSuperfluidのトークンがDepositされていく
- ワンタップでNFTをレンタルできることを伝達（日数の選択をしない）
- 残高が自動的に減り続けていることを伝える
