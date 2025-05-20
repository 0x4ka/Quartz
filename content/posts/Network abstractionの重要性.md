---
title: "Network abstractionの重要性"
date: "1970-01-20T12:01:01.459Z"
tags:
  
---

#WalletContract #Wallet

Abstractionの意味（computer scienceの視点）
- より重要な領域に注意を集中させるために情報を隠すことを意味する

## Optimism, Wintermuteの悲劇
source:
[$15M of Optimism Tokens Stolen After Wintermute Sent Wrong Wallet Address](https://www.coindesk.com/tech/2022/06/09/15m-of-optimism-tokens-stolen-by-an-attacker-after-wintermute-sent-wrong-wallet-address/)
- 2022年6月9日、OptimismはWintermuteによる意図しないウォレットアドレスの伝達によって1500万ドルのガバナンストークンを第三者に誤送信
    - Wintermuteのウォレットに送るはずだったが、Ethereumネットワーク上の同一アドレスに送信してしまった
        - Wintermuteの本来の持ち主と、Ethereumネットワーク上のウォレットの持ち主が違かった
        - この問題は、Contract Wallet のマルチチェーンでも同様に課題<img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>

- Safe によるマルチチェーン環境におけるAA：アドレス編
    - source: [https://safe.mirror.xyz/4GcGAOFno-suTCjBewiYH4k4yXPDdIukC5woO5Bjc4w](https://safe.mirror.xyz/4GcGAOFno-suTCjBewiYH4k4yXPDdIukC5woO5Bjc4w)
    - 1つのアドレスと複数のアドレスの比較
        - 従来のEOAはEVM対応チェーンであれば全て同一の秘密鍵・公開鍵ペアで資産を管理できた
            - [[ECDSA]]
        - しかし、Contractベースになると各チェーンごとに展開・実行される
            - とはいえAA-CWは利便性と使いやすさに期待が集まっている
        - 各チェーンに展開したCWが異なるアドレスを持っていた場合、以下のような事件が起きてしまう
            - [[Network abstractionの重要性#643447a875f26800003f7e33]]
    - クロスチェーンでCWのアドレスが異なる場合の欠点
        - Optimism, Wintermuteのように資産が失われるリスク
        - クロスチェーンブリッジは、両側で同一のアドレスを仮定するものが多いため前提が崩れる
        - チェーンにまたがる複数のアドレス管理は煩雑
    - 解決策
        - ERC-3770: Chain-specific addresses
            - ウォレットの冒頭にチェーン名を付与することで他チェーン同一アドレスへの誤送信を防ぐ
                - 結局、複数のアドレスを管理し続けることは避けたい
        - CREATE2
            - 各チェーンであらかじめ同一のアドレスを生成できるように調整
                - 各チェーンが持っている独自の状態やストレージに影響されて矛盾が生じる場合がある
        - [[MultichainID]]
            - ENSは、マルチチェーンのアドレス解決をサポートしている
                - 1つのENS名をチェーンによって異なるアドレスにマッピングできる
                - [[mycel]]が狙っているのはこれ？<img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>
            - 人間に対する可読性の高い識別子を提供しつつ、各チェーン上のユニークなアカウントに個別の低レベルアドレスを使用する
            - ![image](https://scrapbox.io/files/64344a75dc70ec001bfaa0c6.png)
    - まとめ
        - > 結論として、ユーザーは明らかに、複数のチェーンにまたがる資産を管理するために、単一の識別子のみを持つことを期待している。反実仮想展開（CREATE2）は実現可能なソリューションだが、近視眼的で問題があり、状態ドリフトや不完全性につながる可能性がある。より良い解決策は、ENS名を活用して、単一のユニークな識別子を異なるチェーンの異なる低レベルアドレスにマッピングすることです。この方法は、マルチチェーンにおけるアドレス管理において、より信頼性が高く、使いやすい方法です。

## Multichain（旧: Anyswap）
- 異なるブロックチェーン間の任意の相互作用を可能にするクロスチェーンインフラストラクチャとして生まれた
- SMPCノードによって操作され、下記のサービスを提供
    - ブリッジ
    - ルーター
    - クロスチェーンコントラクトコール
    - NFTブリッジ/ルーター
- サポート
    - 83種類のチェーン
    - 3428種類のトークン
    - ![image](https://scrapbox.io/files/643dfb2fc962ab001c42a315.png)
- 競合
    - Layer Zero
    - Wormhole

## Avocado
source: [What is the "network" used on Avocado? | Avocado Help Center](https://help.avocado.instadapp.io/en/articles/7038824-what-is-the-network-used-on-avocado)
- ネットワーク抽象化プラットフォーム
- > Avocadoはマルチチェーンのネットワーク抽象化を可能にし、Avocado自体はブロックチェーンではありませんが、より良いWeb3体験を提供するためにブロックチェーンのように動作します。Avocadoはネットワークアグリゲーターとして機能し、すべてのEVMネットワークにアクセスし、利用することができます。
- >  Avocadoは、複数のネイティブガストークンを管理する必要性を抽象化し、トランザクションがどのネットワーク上であっても、1つの統一されたガス残高からUSDCでトランザクションの支払いを行うことができるようにします。


