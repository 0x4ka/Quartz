---
title: 'Why we need a Gradual Ownership?'
date: 2023-06-30T05:06:12.000+09:00
tags: 
---

#Gradual #WIP

[English Ver.:](https://scrapbox.io/0x4ka/Why_we_need_a_Gradual_Ownership%3F#646afa7d75f26800004bf3e0)

市場におけるマクロな課題について整理
- 資源（NFT）を必要としている人に（適正な価格で）流通する市場の実現
    - （換言）NFTの最適分配
        - > 最適分配：生産物に売れ残りも品不足もなく、社会全体として、むだなく資本や資源が配分される状態 → 配分効率
    - その実体的な手法は「財産の独占（↔売手の機会損失を減らす）を解くこと」
        - 「価格競争を促すこと」の行き着く先は独占状態の解除である
- 財産の独占が要因としてある
    - 投機勢・コレクターなどといった市場全体から見たマイノリティの存在
        - 目的は「高値で売りたい」「手放さない」
- 市場の均衡価格から大幅にズレた出品は、市場における均衡価格のフィードバックループ（市場の正常化作用）を停滞させる
    - 市場はいくつもの相対取引で成立した売却価格の集合によって、均衡価格が与えられる
        - つまり、ある資産に対する評価は、取引の成立によって事後的に決定される
            - さらに言えば、その資産を取引できる人にしかその資産に対する評価に参加できない
        - また、均衡価格とその周辺の取引価格の分布には、購入される可能性の確率分布が横たわる
            - ![image](https://scrapbox.io/files/642c76befe96ff001ba57637.png)
            - from: [[READING_Should there be demand-based recurring fees on ENS domains?#642c0feb75f2680000875341]]
    - 均衡価格は、マーケットのファンダメンタルによって常に変動している
        - フィードバックループが正常に機能している状態
    - 均衡価格の形成に参加していないホルダー（マイノリティ）は、市場から見ると悪であると言えるのではないか
        - 均衡価格からあまりにも遠い金額でリストしていると相当に購入されにくい
        - 市場から見ればフィードバックループを停滞させる一因
        - 仮に売り手が、取引価格の分散値から見て妥当なくらいだけ最大取引価格（価格弾力性）より高い価格でリストした場合、購入される可能性は比較的高まる
            - 購入された場合、均衡価格が釣り上げられる
            - 市場のファンダメンタルとして上向きの取引が促進されうる
            - これがフィードバックループである（正も負もあり）
- しかし、実際のところ、マイノリティは市場に悪影響を与えていると同時に、売却の機会を損失している
    - 市場にとっても売手にとっても良くないシチュエーション
    - 均衡価格の形成に参加していないのではなく、できない
        - なぜなら、所有権を手放すか所有し続けるかという二値でしか選択することができない仕組みだから
- 所有権の移転の仕組みを Step / binary ではなく、Gradient にすることで均衡価格の形成に参加できるようにする
    - from "step/binary" to "Guradual Ownership"
        - ![image](https://scrapbox.io/files/6449162ee257e2001b42abcd.png) →  ![image](https://scrapbox.io/files/6449163249b537001b9c80e4.png)
    - （仕組みの説明）
    - この場合の均衡価格は、相対取引で成立した売却価格の集合ではなく、1secあたりの貸出価格の集合で形成される
        - 市場が成熟するにつれて、売却価格と時間あたり貸出価格の間には一定の関係性が生まれてくるため、二つの均衡価格は同一の概念で捉えられるようになる
- 結果的に、マイノリティは均衡価格の形成に参加（取引が成立）するため、資源の流通が滑らかになる
- 希少財に限る？
    - 蓋然性が高いアセット
    - 流動性を促進する
    - gradualな所有形態
    - 漸近
- [[流動性が高いということは市場によって正常化される頻度が高いため、より真価に近い評価を得やすくなる]]

memo:
![image](https://scrapbox.io/files/64490f179ed1ab001cd4b53d.png)

事例
- [https://www.wayhome.co.uk/](https://www.wayhome.co.uk/)
- [https://www.altfi.com/article/10651_gradual-homeownership-fintech-wayhome-raises-8-series-a](https://www.altfi.com/article/10651_gradual-homeownership-fintech-wayhome-raises-8-series-a)
    - 27 April 2023


雑記
私はNFT市場におけるマクロ的な課題の一つに、NFTを必要としている人に適正な価格で流通する市場の実現が挙げられると考えています。
言い換えると、NFTの最適分配を実現する必要があるということです。現在のNFT市場は、高額に転売したい投機層によって結果的にNFTが独占されていると解釈することができます。
しかし、それでは価格競争が起きず、手に入れたい人が適正な価格で手に入れられないという事態を招いていると考えられます

一旦、投機層の定義を改めます。
ここでは、市場で行われる数多くの相対取引で成立している売却価格の集合によって得られる均衡価格があります。投機層とは、この均衡価格からあまりにもずれた高値で出品するユーザーたちのことを表現することとします。
またそれらを略してマイノリティとして表現します

そこで、マイノリティがなぜ市場の健全性に悪影響を与えるかということについて説明します。
市場の均衡価格から著しく外れた状態というのは、市場で行われる数多くの相対取引で成立している売却価格の集合における分散の数値よりも外れているということです。
もちろん、均衡価格に比べて高値になるほど購入される可能性は低減します。ここには希望販売価格に対して購入者が受け入れる確率の分布が存在します。

「市場の健全性を維持するためには、市場参加者が均衡価格に近い価格で取引を行い、市場全体の価格形成プロセスが健全に機能することが必要である」ということをより具体的なケースで考えると、均衡価格から大きく外れた値段で出品した場合、多くの人は先ほどの説明した確率分布により購入しません。そうなると、このマイノリティは市場全体の価格形成プロセスに参加していないということになります。これは市場に商品が存在するにも関わらず、実質的に評価に含まれないことになります。
一方で、出品価格を市場における取引価格の最大値よりも僅かに高い価格で出品した場合はどうでしょうか。購入される確率は上がります。仮に購入された場合、市場の均衡価格は僅かに上昇するはずです。この現象が市場の価格形成プロセスへの参加を表すことになります。

このような価格形成プロセスが繰り返されることによって、マーケットの相場の推移が現れてくるということです。

以上のような立場から見ると、均衡価格の形成に参加していないマイノリティは、市場から見ると悪であると言えてしまうのです。しかし、実際のところ、マイノリティは市場に悪影響を与えていると同時に、売却の機会を損失しています。市場にとっても売手にとっても良くないシチュエーションです。
そこで、私は一概にマイノリティが悪いという話でもない気がしているのです。

というのも、マイノリティは均衡価格の形成、言い換えれば市場の価格形成プロセスに参加していないのではなく、参加できない仕組みによってそうなっていると考えています。
なぜなら、現状の取引の形態というのは、所有権を手放すか所有し続けるかという二値でしか選択することができない仕組みであるからです。
ここで、所有と非所有をバイナリーではなく、段階的に移行できる取引の仕組みがあればどうでしょう。
この場合の均衡価格は、相対取引で成立した売却価格の集合ではなく、1secあたりの貸出価格の集合で形成される。市場が成熟するにつれて、売却価格と時間あたり貸出価格の間には一定の関係性が生まれてくるため、二つの均衡価格は同一の概念で捉えられるようになります。結果的に、マイノリティは均衡価格の形成に参加（取引が成立）するため、資源の流通が滑らかになると考えています。


English Ver.:
# WIP_Why we need a Gradual Ownership?
Organize about macro issues in the market
- Realization of a market where resources (NFT) are distributed to those who need them (at a fair price)
    - （Optimal distribution of NFTs
        - > Optimal distribution: A state in which there are no unsold products or shortages, and capital and resources are allocated without waste to society as a whole.
    - The substantive method is to "break the monopoly of property (↔ reduce the seller's opportunity loss)
        - The goal of "encouraging price competition" is to break the monopoly.
- Property monopoly is a factor
    - Minority players such as speculators, collectors, etc. exist in the market as a whole.
        - The goal is to "keep it" or "sell it at a high price
- Listings that deviate significantly from the market's equilibrium price will stall the feedback loop of the equilibrium price in the market
    - The market is given an equilibrium price by the set of sale prices established in a number of relative transactions
        - Also, the probability distribution of the likelihood of being purchased lies in the distribution of the equilibrium price and the surrounding transaction prices.
            - ![image](https://scrapbox.io/files/642c76befe96ff001ba57637.png)
            - from: [[READING_Should there be demand-based recurring fees on ENS domains?#642c0feb75f2680000875341]]
    - Equilibrium prices are constantly changing depending on market fundamentals
        - The feedback loop is functioning properly
    - Holders (minorities) who do not participate in the formation of the equilibrium price can be said to be bad from the market's point of view
        - Listing at an amount too far from the equilibrium price makes it considerably difficult to be purchased
        - From the market's point of view, it is a factor that stagnates the feedback loop
        - If a seller lists at a price that is only reasonably high above the maximum transaction price in terms of the variance of transaction prices, the likelihood of a purchase increases
            - If purchased, the equilibrium price will be inflated
            - Market fundamentals may encourage upward trading
            - This is the feedback loop (both positive and negative)
- However, in reality, minorities are negatively impacting the market and at the same time, they are losing the opportunity to sell
    - Situation not good for the market or for sellers
    - Not that they do not participate in the formation of the equilibrium price, but they cannot
        - Because the system only allows a binary choice of whether to give up ownership or continue to own the property
- Make the mechanism of ownership transfer not step/binary but gradient so that it can participate in the formation of the equilibrium price
    - from "step/binary" to "gradient ownership"
        - ![image](https://scrapbox.io/files/6449162ee257e2001b42abcd.png) -> ![image](https://scrapbox.io/files/6449163249b537001b9c80e4.png)
    - (Explanation of how it works)
    - The equilibrium price in this case is formed by the set of lending prices per sec, not the set of sale prices established in a relative transaction
        - As the market matures, a certain relationship develops between the sale price and the lending price per hour, so that the two equilibrium prices are captured by the same concept
- As a result, minorities participate in the formation of equilibrium prices (transactions are concluded), thus smoothing the distribution of resources.

memo:.
![image](https://scrapbox.io/files/64490f179ed1ab001cd4b53d.png)

### case study
- [https://www.wayhome.co.uk/](https://www.wayhome.co.uk/)
- [https://www.altfi.com/article/10651_gradual-homeownership-fintech-wayhome-raises-8-series-a](https://www.altfi.com/article/10651_gradual-homeownership-fintech-wayhome-raises-8-series-a)
    - 27 April 2023
