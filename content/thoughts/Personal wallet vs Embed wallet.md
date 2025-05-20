---
title: Personal wallet vs Embed wallet
date: 1970-01-20T11:36:08.280Z
tags: 
---

#wallet
embed wallet ≒ [[dApp Wallet]]

[https://zengo.com/personal-wallets-vs-embedded-wallets-who-wins/](https://zengo.com/personal-wallets-vs-embedded-wallets-who-wins/)
STEPNのようなウォレット
- アプリケーションのUIに組み込まれたカストディアルウォレット
    - あるいはMPCを用いたセルフカストディウォレット

- 1アプリ＝1ウォレット＝1パブリックアドレス
    - あるアプリケーションを使う分には便利になる
    - メルカリへの入金も近い
    - CEXの入金も近いか
![image](https://scrapbox.io/files/645612973d0eeae58d9e5e66.png)

一応集合としては下記のようになるのか？
- Personal
    - EOA
    - MPC
    - CW
- Embed（castody?)
    - EOA
    - MPC
    - CW

- dapp walletのcons
    - ウォレットの仕組みについて学べる機会を得られない
    - 技術的にはセルフカストディアルであるが、ウォレットの仕組みを理解しないユーザーにとってアプリケーションはカストディアンであること
    - ウォレットに資金を投入する必要が出てくる場合がある
    - ソーシャルログインやメールアドレスログインに依存する
    - ユーザーは、何十から何百のウォレットと公開アドレスを持つことになり、資産を分散して管理する必要に迫られる
    - > [結論から言うと組み込み型ウォレットは、最初は目に見えずシンプルになりますが、数十から数百のDappsにまたがって所有する資産を大規模に乱立させることで、個人のセキュリティと複雑さの底辺への競争を招きます。](https://zengo.com/personal-wallets-vs-embedded-wallets-who-wins/#:~:text=結論から言うと組み込み型ウォレットは%E3%80%81最初は目に見えずシンプルになりますが%E3%80%81数十から数百のDappsにまたがって所有する資産を大規模に乱立させることで%E3%80%81個人のセキュリティと複雑さの底辺への競争を招きます%E3%80%82)

- > ユーザーがより多くのDapps、より多くのコイン、より多くのブロックチェーン、より多くのシンプルな組み込みウォレットを使用するようになるにつれ、これらすべてをナビゲートする主要なインターフェースがますます重要になるでしょう。
    - マジでそう思う<img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>
    - > Dappsが組み込みウォレットを提供したとしても、ユーザーはより安全な統合アカウントにアイテムをチェックアウトして引き出し、他のDappsで使用したり、スワップ、ステーク、販売、保管、送信、レンタル、共有、委任、そして・・・なぜか・・・税金を支払うことを望んでいます。組み込み型ウォレットは、重要な機能セットと同等になることはなく、貴重で高価な資産を保持するのに十分なものではありません。検索エンジンと比較するのがよいでしょう。すべてのウェブサイトには専用の検索機能がありますが、そのどれもがGoogleの実用性、パワー、信頼に匹敵するものではありません。
        - dappがウォレットを独自に持っている状態が前提となり、アグリゲートするwallet interfaceが必要になると言っている
            - アプリケーションはモジュールを持てばいいのではないか？
                - CWでwallet本体とproxyに構成が分けられ、後者が各ユーザーに割り当てられ、wallet本体はsingletonであるような状態だとどうか？アプリケーションがsingletonをある決まったI/Fで作る?<img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>
                    - これはダメそう<img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>

