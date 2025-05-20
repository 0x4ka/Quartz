---
title: "Blur の BLENDER の Unlock Ownership の実装について"
date: 2023-05-15T08:29:00.000+09:00
tags: 
---

- Blur.io が新たに発表した NFT Lending protocol の Blender は BNPL 機能を持っている
    - BNPLでは本体価格の2割で購入することができ、残りの8割はローンで購入している状況らしい
    - そのため、ローンを完済するまではNFTの本来の所有権はロックされているらしい
        - これがどういう状況のことを示しているのかわからない
        - どうやら、購入すると同時に担保として融資を受けて支払っているらしい
            - なので、Vaultに担保としてロックされている状態になっている
            - Refundすればロックを解除（担保を引き戻し）できる
        - つまり債務を取引しているような状態<img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>
        - というよりも単純に担保として預けたNFTの権利を取引してるといった方が近い
> [@blur_io](https://twitter.com/blur_io/status/1653101795546374144?s=20): 7/ After making your BNPL purchase, you can repay your borrow at any time to take full ownership of your NFT. Or, list your NFT any time and keep any profit when you sell.
> ![image](https://pbs.twimg.com/media/FvD_Ub4agAA3zFv.jpg)

