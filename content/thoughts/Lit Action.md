---
title: Lit Action
date: 1970-01-20T18:14:33.828Z
tags: 
---

#WalletContract
source: [/masatojames/Lit Protocol#64321d285beced0000af74ba](https://scrapbox.io/masatojames/Lit Protocol#64321d285beced0000af74ba)

- Lit Protocol独自のスマートコントラクト
    - 実態はIPFSに保存された不変のJavaScriptのコード
    - Litの閾値暗号ネットワーク上で実行されるJavaScript関数。JavaScriptのスマートコントラクトであり、PKPと組み合わせることで、取引やその他の任意のデータに署名するようにプログラムすることができます
    - > 実現できる制御の例
    - >  「n以上のEtherを保有していること」というオンチェーン条件を満たすユーザーにのみ暗号化された静的コンテンツの復号鍵を提供する
    - >  「ユーザーはNFTを保有していること」といったオンチェーン条件を満たしたユーザーにのみ、署名を提供する。
    - >  Google OAuth、Discordなどのオフチェーンサービスの認証情報をみて、オンチェーン取引を実行する