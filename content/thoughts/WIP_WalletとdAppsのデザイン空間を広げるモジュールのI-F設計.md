---
title: "WIP_WalletとdAppsのデザイン空間を広げるモジュールのI/F設計"
date: June 19, 2023
tags: 
---

#wallet #WalletContract

関連: [[WIP_A module market for Contract wallet]]

棄却: [[既存の Contract Wallet にwrite操作を禁止するモジュールを加えても被Approvalユーザーにバイパスされ得る]]

- dAppを承認することで、対象のNFTやFTといった資産を自動的に支払い・運用するだけでなく、ロックアップすることができるようなモジュールの設計
    - コントラクトウォレットに採用されている基本機能に加えて、
        - 自身が保有する FT や NFT をロックする（譲渡不可能な状態にする）
        - 自身が保有する FT や NFT を譲渡可能なアカウントのホワイトリストを設定する
        - 承認のセッション管理
    - 上記のような機能をdApp側から強制するような仕組みを取り入れたい
        - 他のモジュールの影響や新たなモジュールに差し替えられることを除外できない
            - [[Firewallet]] の場合は、DAOがウォレットのパーミッションを割ることで各ロールに合わせた利用範囲を定められる機構を持っている
                - 今の所 Firewallet は利害関係が一致しているコンテキスト上でできることを分割するアプローチなので、RentaFi のような貸し借りの間に一定の Trust が無いケースを想定しきれていません。by  taxio
        - つまり単にModuleを登録するだけでなく Module 同士の有効・無効の制御が必要？
            - Wallet ↔︎ module という1:Nの関係性から、Wallet ↔︎ (module_A ⇄ module_M) というモジュール同士の相互作用が必要
                - 例えば、レンタルした資産をロックアップするmoduleとNFTを送信するmoduleがある場合、ロックアップ中のNFTについては承認されたModule以外は操作できないようにしなければならない
                - Argentの場合、資産をロックするような仕組みがあるが特定アセットに対してではなくウォレット丸ごとロックされる

- かつてRentableというNFTレンタルプロトコルは、コントラクトウォレットを使用することで無担保かつオリジナルNFTを貸し出す仕組みを構築した
    - ReadOnly な Smart Wallet
    - 提供方式から分類すると Embed wallet といえる
        - ユーザー体験：特定のアプリケーションに利用が制限される
        - ガスコスト：EOAに比べて高い（デプロイコストもかかる）
        - 操作性：例えReadOnlyであってもWallet Connect  周りの操作をしないといけない
- CWをアプリごとに作成してしまうと、ユーザーは将来的に無数のウォレットを管理し続けなければならない
    - 埋め込み型ウォレット共通の課題間
        - [[Personal wallet vs Embed wallet]] / [[App-specific CW will be as chaotic as App Embed Wallet]]
- CWを前提とするdAppはModuleに実装内容を切り出していくべき
    - ![image](https://scrapbox.io/files/6457d0543531e9c482da4591.png)
        - each module holds a reservation storage and BaseWallet check it before transaction. But Scalability is lacking
        - それにストレージが各モジュールの実装に依存してしまう
            - ストレージはウォレット側で持っていた方がいい
    - ![image](https://scrapbox.io/files/6457d7f375c3b17883af0347.png)
        - こんな設計はどうだろう？
        - 現時点のSafeはユーザーが自分でGuardを切り替えられてしまうため、対策必要
            - 正確にはGuardの変更には、既存Guardによるcheckが入るため制御できる
            - しかしmoduleを利用してbypassできてしまうため別の対策が必要
        - GuardをロックするためにdAppを承認するロジックを追加する
        - この際、Guardは複数追加できるようにした方が便利なはず
            - Guradualのguardだけロックしたい
            - もはやGuardではなく、別の検証ロジックを追加しても良いかも
- 課題
    - どのようにモジュール同士の相互作用を整理するか

