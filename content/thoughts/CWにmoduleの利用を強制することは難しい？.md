---
title: "CWにmoduleの利用を強制することは難しい？"
date: April 26, 2023
tags: 
---

#wallet

論点
- dAppがCWに対して特定のtransactionの実行を阻止するにはdApp側からCWに正しいBlockが実装されているか認知する術がない説
    - Interface は同じでも内部の実装はわからない
    - bytes code を全て検証しなければいけない

シーン
- contract wallet と module
    - 各dAppが独自に module を実装して利用してもらうような仕組みを想定
        - Rental marketplace でオリジナルNFTをCWで receive する際に、Receiver がオリジナルNFTを移転できないようにCWのTxを検証する

別解（ダメだった）
- それぞれが module をデプロイして利用する場合、同一 Interface でありながら内部のロジックが変更されているリスクがある
    - module を各チェーンに1つだけ deploy し、CWがその module を call すれば良い？
- 結局、正しい module を call しているかどうかを知る由はない

現状の結論
- dAppがCWの開発…提供をしなければならない

