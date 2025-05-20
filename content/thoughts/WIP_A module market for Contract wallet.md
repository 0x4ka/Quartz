---
title: "WIP_A module market for Contract wallet"
date: 1970-01-20T18:19:18.949Z
tags: 
---

#wallet #WalletContract

ref: [[WIP_WalletとdAppsのデザイン空間を広げるモジュールのI/F設計]] MUST READ

> dApps will penetrate into Wallet UX. Modules can abstract dApp experience.

- CWはコントラクトの性質上、機能拡張をしやすいようにモジュール型のアーキテクチャを採用している
    - 現状はWallet provider側によってmoduleの設計が行われているが、それはウォレット所有者あるいはコミュニティにおける自治
    - コントラクトのコンポーザビリティの特性を活かすことを考えるとアプリケーション側からmoduleの提案が起こってくるだろう
    - Module Market の誕生が考えられる
    - ![image](https://scrapbox.io/files/6453fd2db5282c52c449e13d.png) ![image](https://scrapbox.io/files/6453fd363654c76d6f6fce85.png) ![image](https://scrapbox.io/files/6453fd4b3c9ba4093107ab46.png)
    - ![image](https://scrapbox.io/files/65c747fc22b03800245d6989.png)
    - ![image](https://scrapbox.io/files/65c74804a116370026d38f08.png)
![image](https://scrapbox.io/files/65c74823e0b46500257f2c00.png)


- モジュールとウォレット本体の統合は、各種プロダクト独自に設計されている
- moduleの扱い方の規格化をしたい
    - Safe
        - Safe は、ウォレットコントラクトに任意の [[Safe Module]] を設定することができる
            - module を通して wallet 本体を呼び出す構造になっている
            - [[WIP_Safe Guard]] は、Wallet 本体のトランザクションの実行前後に検証を行う設計
    - Argent
        - [[argent]]
        - moduleからwalletの機能を呼びだす
        - modul(singleton)→proxy→wallet(singleton)→dapp
        - moduleが最初のタッチポイントなので、basewalletに検証機能のIFとロジックを実装し、moduleでIFを採用して検証しなければいけない？
            - argentは、moduleとbasewalletを機能的に独立させることを目指しているため、moduleがbasewalletの仕様に依存してしまうのは本来の設計上相性が悪いのでは<img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>
    - unWallet
        - [[unWallet の Module アーキテクチャ]]
        - Module Manager が定義されている点が Argent と異なるポイント
        - しかしModule Manager はウォレットオーナーによって自由に変更可能
    - avocado
        - [[Avocado Wallet のソースコード]]
        - [[How avocado is non-custodial]]
- 自分のビジョンとしては、アプリケーションは、dApp本体とmoduleを提供する
    - 乱立するWallet戦争を波乗りする
    - ![image](https://scrapbox.io/files/6458840072a971c2ae58368a.png)
        - Module market
- Module market の萌芽
    - backpackのxNFT
    - ![image](https://scrapbox.io/files/6453ff48ebf7044a3d42ff9a.png)

