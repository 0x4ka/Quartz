---
title: "Sodium"
date: April 10, 2023 (TZ: UTC+9)
tags: 
---

#NFTFi
[https://sodium.fi](https://sodium.fi)

P2Pの柔軟性とP2Poolの効率性を組み合わせることで、NFT流動性プラットフォームの障害を解決
- 高度なローンリクエストのマッチングメカニズム
- SODIUM独自のLending AMM
- Sodium Walletを通じたアセット有用性の維持

>  借り手は、2種類のローンリクエストから選択することができます：
>  スタンダードローン：あらゆるNFT担保に裏打ちされ、柔軟な期間設定、即時流動性はありません。
>  インスタントローン： 既存のレンディングプールの少なくとも1つによってサポートされているNFTに裏打ちされ、最大30日間の期間、即時流動性が利用可能 です。

![image](https://scrapbox.io/files/642fd8007f6c6f001b18ffc8.png)

Borrowerのアクション（スタンダードローン）
1. NFTを担保にいくら借りたいか
2. 借入期間
3. 初回金利

借りてはNFTをSodium Walletにうつし、ローンリクエストを発行する
- ローン期間中、有用性を維持するが譲渡や売却はできない

インスタントローン
1. 借入金額
2. 借入期間

ローンフルフィルメント
- ローンリクエストで設定した初期APRは時間の経過とともに段階的に増加する
    - Lenderへのインセンティブ
    - 48h制限
![image](https://scrapbox.io/files/642fdb06d26465001cfea871.png)

レンディングの成立の仕方
> The Borrower can partially or fully accept a loan at any time during the Loan Request fulfillment process by choosing a Loan Offer where the average APR meets the Borrower's expectations.
- 借手は、ローンオファーの中から希望するAPRに合わせて取捨選択できる
    - 貸出は、リクエストに対して満額でも部分的でもOK
    - eg. 借手は8ETHを借りたいとする（APR 18.75%）
        - 異なる2者の貸手から借入が成立する
        - APRは両者の加重平均となる
            - $\frac{5ETH \times 15\% + 3ETH \times 25\%}{5ETH + 3ETH}$
- ![image](https://scrapbox.io/files/642fde56d24573001bca02e3.png)

ローンの返済方法
> The Borrower shall partially repay or repay the loan in full before the end of the agreed upon period; when making early principal repayments, the Borrower must also pay at least half of the corresponding interest due.
>  Partial repayments are distributed to Lenders starting from the top of the Lending Queue, resulting in decreasing average APR for the Borrower.
>  Once repaid, the Borrower may reclaim their collateral.
![image](https://scrapbox.io/files/642ff05df44ef9001be28597.png)

精算方法
- オークション
    - buy it now　で購入する人がいれば即座に落札される
- 誰もbuy it now で購入しない場合、精算オークションは24時間で終了
    - 最高入札者が落札する
        - bidするにはETHをコントラクトにdepositする
            - depositされたETHでレンダーの負債を決済する
    - 入札が0の場合は、担保は Lending Que の最初のレンダーに移される
        - > the collateral will be transferred to the first Lender in the Lending Queue, as the liquidity they provided acts as a bid by default.
    - どんどん価格が下がっていくため、高い評価額でLendしたLenderが割を食うことになる
        - その代わりNFTが手に入る
        - ![image](https://scrapbox.io/files/642ff19896d2b9001c5953e1.png)



