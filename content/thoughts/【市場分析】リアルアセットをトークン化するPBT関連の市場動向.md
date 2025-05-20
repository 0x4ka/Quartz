---
title: 【市場分析】リアルアセットをトークン化するPBT関連の市場動向
date: 1970-01-20T07:55:37.866Z
tags: 
---

事例
- PBT
- Courtyard（[https://docs.courtyard.io/courtyard/logistics-and-legal/asset-storage-and-insurance](https://docs.courtyard.io/courtyard/logistics-and-legal/asset-storage-and-insurance)
- Tickeme

課題
- セキュアな管理体制（物理アセットの管理をどう保障されているか？）
    - 銀行レベルの金庫と輸送時・管理時の保険を適用している（すごい）
    - [https://us.brinks.com/](https://us.brinks.com/)
- プロダクトとの結びつき（NFTと物理アセットの紐付きをどう保障するか？）
    - PBTは埋め込んでいる
    - 剥がされてはいけない

[https://blog.cryptostars.is/what-are-pbts-physically-backed-tokens-and-why-you-should-care-827a037c3f93](https://blog.cryptostars.is/what-are-pbts-physically-backed-tokens-and-why-you-should-care-827a037c3f93)


リアルアセットとNFTを紐づける新たな領域の萌芽をのぞく

2022年10月17日に、 #AZUKI は #ScantoOwn を実現する #PhysicalBackedToken  ( #PBT ) の規格を発表しました。

主に、AZUKIが今後展開するリアルアセットをNFTと紐付け、クリエイターやコミュニティのための新たな体験を生み出すことを目指しています。まず最初にPBTを用いたプロダクトとして「 Azuki Golden Skateboard」が発表され、オークションが実施されました。

[https://twitter.com/AzukiOfficial/status/1583624250493394944?s=20&t=ojdYKnY2t9VAvX2jLdp5mA](https://twitter.com/AzukiOfficial/status/1583624250493394944?s=20&t=ojdYKnY2t9VAvX2jLdp5mA)
Azuki公式Twitterから引用

[https://twitter.com/NftPinuts/status/1584034729208127491?s=20&t=ojdYKnY2t9VAvX2jLdp5mA](https://twitter.com/NftPinuts/status/1584034729208127491?s=20&t=ojdYKnY2t9VAvX2jLdp5mA)

さらに11月3日には、Y Combinatorでアクセラレートされていた #Courtyard が$7Mの調達を実施しました。CourtyardもAZUKIと同じようにNFTとリアルアセットを紐付けることで、プロダクトの新しい流通のあり方を実現しようとするサービスです。

[https://www.businessinsider.com/courtyard-y-combinator-web3-nfts-startup-vc-funding-nea-brinks-2022-11](https://www.businessinsider.com/courtyard-y-combinator-web3-nfts-startup-vc-funding-nea-brinks-2022-11)

これらのプロダクトは、どちらもリアルアセットをNFTと紐付けて取引の流動性を高めたり、デジタルコレクションとしてコミュニケーションを促したりすることに取り組んでいますが、それぞれの取り組みの力点は大きく異なっています。

後程それぞれについて説明しますが、
・AZUKIは、リアルアセットとNFTの紐付けに力点があり、
・Courtyardは、NFT化したリアルアセットの保証に力点があるようにみえます。

NFTがデプロイされているブロックチェーンから、ブロックチェーンの外側にあるモノを参照するか、またどのように信用を保証するかという問いは、今回のAZUKIによるPBTやCourtyardによるリアルアセットの保障の取り組みに始まったことではなく、広くはオラクル問題として語られてきた取り組みと言えるでしょう。

本記事では、リアルアセットとNFTの紐付けを行う各プロダクトの取り組みを概観しつつ、それらに関わる技術、管理する上での課題について整理します。

AZUKIによるリアルアセットとNFTの紐づけについて

AZUKI Physical Backed Token and Golden Skate Board

リリース：2022年10月17日
公式記事：[https://www.azuki.com/updates/pbt](https://www.azuki.com/updates/pbt)
twitter：[https://twitter.com/AzukiOfficial](https://twitter.com/AzukiOfficial)

AzukiはプロダクトとNFTを紐づけるためのトークン規格『Physical Backed Token』と物理チップ『BEAN Chip』をセットで発表しました。

PBTとは、ブロックチェーン上のデジタルトークン（NFT）を、現実世界のリアルアセット（製品）と結びつけるためのオープンソースのトークン規格です。これまでNFTとリアルアセットを紐づける場合、各事業者による中央集権的なデータベースやサーバーに依存していましたが、PBTはトークン規格と合わせて物理チップ「BEAN Chip」を提案することで分散的な紐付けを実現しようとしています。

[https://blog.cryptostars.is/what-are-pbts-physically-backed-tokens-and-why-you-should-care-827a037c3f93](https://blog.cryptostars.is/what-are-pbts-physically-backed-tokens-and-why-you-should-care-827a037c3f93)

PBTとの紐付けが可能なチップはBEAN Chipだけではなく、以下の要件を満たしていれば利用可能なようです。

#ECDSA secp256k1 非対称鍵ペアを安全に生成・保管する機能

非対称鍵ペアの秘密鍵からメッセージに署名する機能

非対称鍵ペアの公開鍵のみを取り出すことができる（秘密鍵は取り出せない）

これによって、PBTを転送する際にリアルアセットの所有が求められ、Scan to Own機能によって署名されることで初めてPBTの転送が可能となります。つまり、現物の移転とPBTの移転が同期するような仕組みを実現しています。

より詳しく言えば、以上の要件を満たしたチップを用いることで、

各NFTと物理チップとリンクされる

NFTはチップによる署名が実行された場合のみ譲渡可能

詳細は、PBTの公式サイトおよびリポジトリを参照することをおすすめします。

PBTと物理チップを組み合わせて利用することで、製品ライフサイクルにまたがってリアルアセットとNFTを紐づけることができるようになっているわけです。

しかし、製品にどのようにチップを埋め込むかについては依然として慎重に検討されるべきだと筆者は考えます。

今回のスケートボードの場合は、内部に埋め込まれているため破壊しなければチップを取り出すことができないため比較的成立していると考えられますが、これには製品自体に求められる要件（素材、強度、復元の容易性など）も関係してくるためです。

CourtyardによるリアルアセットのNFT化と保障について

Courtyard

リリース：2022年10月23日
Medium：[https://medium.com/courtyard/introducing-courtyard-398592397061](https://medium.com/courtyard/introducing-courtyard-398592397061)
サービスページ：[https://courtyard.io/](https://courtyard.io/)
ドキュメント：[https://docs.courtyard.io/courtyard/about-courtyard/what-is-courtyard](https://docs.courtyard.io/courtyard/about-courtyard/what-is-courtyard)

公式サイトより引用

[https://courtyard.io/](https://courtyard.io/)

Courtyardは、リアルアセットをBrink'sが提供する保管庫に発送することでコレクショングッズをNFTとして流通させることができるサービスです。

リアルアセットとNFTを紐づける際のもう一つの課題として、誰がプロダクトの存在を保障するのかという観点がありますが、Courtyardのアプローチはこれに応える堅実なソリューションを提案しています。

AZUKIは、「プロダクトとNFTの1:1対応」と「流通状態の紐付け」が主なソリューションでしたが、Courtyardの場合はプロダクトの存在をどのように保障するかという課題に対して応えたサービスであり、そのアプローチには大規模事業者が本格的にweb3領域に参入する時代の転換を感じさせます。

冒頭で少し触れましたが、Courtyardを利用してプロダクトをNFT化したいユーザーは、Brink'sが提供する保管庫にプロダクトを発送するのですが、そのBrink'sは、世界で最も信頼できるセキュリティを誇る貴重品を専門に扱う警備輸送会社です。

発送されたプロダクトは輸送時・管理時の警備輸送はもちろん、輸送時の保険も提供しています。これにより、高額なコレクションを安全にNFT化できるというわけです。

[https://us.brinks.com/](https://us.brinks.com/)

保管庫に届いたプロダクトは、認証された後にCourtyard側で3Dスキャンされ「Connected Collectible」としてNFT化されます。プロダクトのオーナーは、NFTのクリエイター兼ホルダーとして所有権を獲得します。その後は、HODLするも販売するも自由です。もちろん二次流通におけるロイヤリティ（取引価格の1%）も獲得することができます。

また、Connected Collectibleは、いつでもプロダクトと交換することが可能です。プロダクトのオリジナル所有者は、売却していないConnected Collectibleから手数料なしでプロダクトを償還することができます。つまり、出品者はリスクを負うことなくNFT化をお試しできます。

Nicolas le Jeuneによる【Introducing Courtyard】から引用

このようにCourtyardは、既存の警備輸送・保管庫業者とタッグを組むことで、リアルアセットとNFTの紐付けをする際に生じる「プロダクト保障の課題」に対するソリューションを展開しています。

Courtyardのアプローチは、AZUKIが志向した分散型の紐付け方とは反対を向いた特定事業者のサービスに依存した中央集権的なアプローチではありますが、ユーザーの資産を保護する観点や利用しやすさの観点を交えて考えると、このような折衷案も様々なサービスで採用されてほしいと感じます。

リアルアセットとNFTを紐付けるアプローチと課題

本記事では、リアルアセットとNFTを結びつける2つのプロジェクトを紹介しつつ、それぞれのアプローチについて考察を交えて紹介しました。

再掲すると、どちらもリアルアセットをNFTと紐付けて取引の流動性を高めたり、デジタルコレクションとしてコミュニケーションを促したりすることに取り組んでいますが、それぞれの取り組みの力点は大きく異なっていました。

・AZUKIは、リアルアセットとNFTの紐付けに力点
・Courtyardは、NFT化したリアルアセットの保証に力点

依然として、物理チップの装着方法や素材等による影響や特定事業者に依存するスキームに課題は残ります。

しかし、国内でもUniCaskやCYPHER、TicketMeといったプロジェクトがリアルアセットとNFTを絡めた展開を進めていますし、今後もこういったプロジェクト自体は増えていくと考えます。

これら国内外での取り組みがどのように受け入れられていくのか、製品ライフサイクルとの関わりがどのように改善されていくのか、今後の動向に期待です。
