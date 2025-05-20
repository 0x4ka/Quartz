---
title: 'How avocado is non-custodial'
date: 2023-05-07T05:36:42.000+09:00
tags: 
---

#WalletContract #wallet
source: [How Avocado is non-custodial](https://blog.instadapp.io/avocado-non-custodial/)

- なぜEOAからavocado wallet に資産を入金する必要があるのか
    - 中央集権的な取引所のUXに似ているが、どのアドレスも、avocadoでさえもユーザーのウォレットにアクセスすることはできません
    - EOAは、コントラクトウォレットを生成/アクセスするためのキーとして利用される
- avocadoでの取引はどのような処理を経るのか
    - コントラクトウォレットはメッセージに署名（AA）し、avocadoのRPCを経由してそれぞれのブロックチェーンに取引を送信するために利用可能なbroadcasterを探す
    - 複数のbroadcasterが利用可能であるため、ある1つがダウンしても耐える冗長性があります
        - ![image](https://scrapbox.io/files/64357a23c4fba2001c317499.png)
- 署名の仕方
    - Metamask使ってない？<img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>
    - UserOpを作るために必要
        - ![image](https://scrapbox.io/files/64357a4ede139e001bf510b4.png)

other
- [[Gas Abstraction]]
- [[network abstractionの重要性]]
- [[Avocado Wallet のソースコード]]
