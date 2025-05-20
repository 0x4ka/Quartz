---
title: '【市場分析】OpenSeaによるロイヤリティツールとNFTマーケットプレイスの反応'
date: 2022-11-23T05:26:00.000+09:00
tags: 
---

[[【時系列まとめ】NFTマケプレのクリエイターロイヤリティに関する動向まとめ]] からソース情報を引っ張っている

### 目次
- 要約
- NFT市場を取り巻くロイヤリティ問題
- Operator Filter Registryについて
- ツール発表を受けたNFTマーケットプレイスの反応
- おまけ：Immutable Xによるロイヤリティ分配ツール

### これまでのロイヤリティ問題
- ERC1271? によってロイヤリティに関するインターフェースは共通化されたが、支払いの執行についてはマケプレに依存していた
    - コントラクトにロイヤリティの支払いを強制するロジックを含める難しさもあった
    - 販売と転送の違いをコントラクトでどう処理するか？

NFTは、クリエイターがデプロイしたチェーンのエコシステムが存続する限り二次流通に対するロイヤリティ収益を得ることができる点で大きな注目と期待があてられていました。
ここで表現するロイヤリティとは、二次流通時に取引額の数%がクリエイターに分配されることを指しています。

しかし、sudoswapによるロイヤリティの非サポートをきっかけに、X2Y2ならびにMagic Edenがロイヤリティ支払いを購入者に選択させる方針を採用するなど、NFTのロイヤリティ神話が崩れかけています。
（ここで尾形さんの関連記事挿入）

そもそも、なぜNFTマーケットプレイスごとにロイヤリティの支払いに差が生じるのでしょうか？これを紐解くには、コントラクトの仕組みに目を向ける必要があります。

### ロイヤリティの仕組みとEIP-2981
NFTを構成しているコントラクトには、そもそもロイヤリティを分配する仕組みは実装されていません。これには、コントラクト側ではNFTを「単純に送付するのか」「売買の結果として送付するのか」という判断ができないことに起因します。NFTの標準規格であるERC721には、売買専用の機能はなく全て送付という基本的な機能を利用しています。

そのため、OpenSeaやLooksRareなどは、各マーケットプレイスが持つオフチェーンのデータベースを用いてロイヤリティ分配を実現しています。
これでは各マーケットプレイスで、ロイヤリティに関する設定を独自に保存しておく必要がありますし、ロイヤリティに関する設定の透明性に疑惑が残ります。このような課題感からロイヤリティに関する設定（ロイヤリティ金額、振込先ウォレットアドレス）をコントラクト上に保存するための拡張標準規格EIP-2981が普及し始めています。
鋭い方はここまでの説明を聞いて「EIP-2981でも分配に関する根本的な問題を解決してないじゃないか」と悟ったかと思います。まさにその通りで、今回のロイヤリティ論争もオフチェーン処理による"余白"がもたらしたと言えるでしょう。

この論争にある種の着地点をもたらしたのがOpenSeaです。数ヶ月の沈黙の末にロイヤリティを半ば強制するツールを公開しました（強気）。



### OpenSeaが発表したツールOperator Filter Registryについて
- 前提として、これは大きなシステムではなく単純なコードスニペット
- コントラクト内で支払いロジックを書き込んでいるわけではない
- 依然としてマケプレ依存ではあるが、ロイヤリティ対応しないマケプレのエスクローコントラクトを名指し（Address指定）で排除するレジストリを提供
- 少し技術的な解説を入れる
    - コントラクトアドレスの指定
    - なぜこれでトランザクションを排除できるのか解説
- 課題
    - 一定のトランザクション

まず前提として、これは大きなシステムではなく単純なコードスニペットであり、コントラクト内で支払いロジックを実装している訳でもありません。なので、先ほど取り上げた根本問題を解決しているか？というとしていません。その代わりに、ロイヤリティ対応しないNFTマーケットプレイスのコントラクトアドレスを名指しし、トランザクションを行わないような処理を実装しています（強気）。

具体的な仕組みについて理解するためにロジックを覗いてみましょう。
- 要となるのはOperatorFilterRegistry
    - ここでregistrantとoperatorのアドレスを引数にした検証用メソッドが定義されている（[https://github.com/ProjectOpenSea/operator-filter-registry/blob/main/src/OperatorFilterRegistry.sol](https://github.com/ProjectOpenSea/operator-filter-registry/blob/main/src/OperatorFilterRegistry.sol) ）
- OperatorFilterは、OperatorFilterRegistryをインポートしてModifierを定義している（[https://github.com/ProjectOpenSea/operator-filter-registry/blob/main/src/OperatorFilterer.sol](https://github.com/ProjectOpenSea/operator-filter-registry/blob/main/src/OperatorFilterer.sol) ）
- NFTは、operatorFiliterをインポートして、modifierをapprove系、transfer系のメソッドに追加するイメージ（[https://github.com/ProjectOpenSea/operator-filter-registry/blob/main/src/example/ExampleERC721.sol](https://github.com/ProjectOpenSea/operator-filter-registry/blob/main/src/example/ExampleERC721.sol) ）
- トークンで規格化される機能とマネタイズ手法は全く異なるという難しさを感じる



### Openseaのツール発表の煽りを受けて方針転換したマケプレ
以上のOpenSeaの動きを受けて、元々ロイヤリティの支払いを購入者に委ねていたBlurとX2Y2はその方針を転換しました。

X2Y2は、9月頭時点でホルダーによる投票によってロイヤリティの支払いを決定する柔軟なロイヤリティシステムを採用していました。しかし、OpenSeaによる発表とそれに賛同するクリエイターの動向を見て、ロイヤリティを適用する方針に転換しました。わずか数ヶ月での方針転換ではありますが、矢面に立ち施策を打ち続けていたX2Y2が個人的に好きです。一方、OpenSeaの振る舞いは強者ですね。
![image](https://scrapbox.io/files/637dab4c5fe94d001efeac43.png)
[https://twitter.com/the_x2y2/status/1565662140404490241](https://twitter.com/the_x2y2/status/1565662140404490241)
X2Y2公式Twitterアカウントから引用

![image](https://scrapbox.io/files/637dabb8751586001da351ec.png)
[https://twitter.com/the_x2y2/status/1593631419561304067?s=20&t=BgB0Av4NQccnXCPWSxLQjg](https://twitter.com/the_x2y2/status/1593631419561304067?s=20&t=BgB0Av4NQccnXCPWSxLQjg)
X2Y2公式Twitterアカウントから引用

同じようにBlurもロイヤリティを擁護する方針に変更しました。
元々Blurのロイヤリティの仕組みはOpenSeaや他のマーケットプレイスと違い、ロイヤリティを支払う代わりにエアドロップによる報酬を受け取ることができるという独自のインセンティブ構造を用いていました。
![image](https://scrapbox.io/files/637dae9d795dfc002195c855.png)
[https://mirror.xyz/blurdao.eth/2nba-2j0zHPrBX0iPSNGquZ9s_WotNH6B4e5usz85mM](https://mirror.xyz/blurdao.eth/2nba-2j0zHPrBX0iPSNGquZ9s_WotNH6B4e5usz85mM)
『Blur is LIVE!』から引用

しかしOpenSeaの発表により、当該ツールを利用して出品を許可しないNFTコレクションに対しては強制的にロイヤリティの支払いを課すことを発表しました。
![image](https://scrapbox.io/files/637dae84795dfc002195c805.png)
[https://twitter.com/blur_io/status/1592203726655086592](https://twitter.com/blur_io/status/1592203726655086592)
Blur公式Twitterアカウントから引用

筆者の考えとしては、NFT総取引額のクリエイターはロイヤリティを得られる"可能性が高い"プラットフォームを利用する方が自然であること、今後拡大を続けるマーケットに貼るのであればNFTの供給側でイニシアチブを獲得できた方がGMV拡大に結びやすいことからOpenSeaの発表は、強気な逆張りであり、他のマーケットプレイスも追従せざるを得なかったと考えます。


おまけ：Immutable Xのロイヤリティ分配について
リサーチするまで知らなかったのですが、Immutable Xもロイヤリティ分配に関するツールを公開していました。本記事では概要だけご紹介いたします。
（概要）
