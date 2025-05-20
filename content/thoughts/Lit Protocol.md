---
title: "Lit Protocol"
date: May 5, 2023
tags: 
---

#wallet

- 暗号鍵ペアの作成と管理を分散して行うことで、条件付き暗号化やプログラムによる署名の実現を目的としたプロトコル
    - source: [Lit Protocolの技術的概要と価値](https://zenn.dev/moneyforward/articles/8c666a192b88bd)
    - ![image](https://scrapbox.io/files/643417b631e952001bfe75ec.png)
    - Lit Protocolの価値
        - > ブロックチェーン上に載せられない機密情報の安全な分散管理
        - >  誰も完全な秘密鍵を持たない状態でのプログラムによる署名
        - >  オンチェーン/オフチェーンのデータを活用した鍵の所有権や利用権の譲渡や制御
        - これまで、鍵管理プロトコルでは、鍵は一元的に管理されることが一般的
            - 鍵の漏洩やセキュリティ侵害のリスクが高まる
        - Lit Protocolでは、機密情報である鍵を分散管理することが可能
            - 鍵の漏洩やセキュリティ侵害のリスクを大幅に削減
        - NFTなどを用いて鍵の所有権や利用権を証明し、ブロックチェーン上で権利の譲渡や制御が可能
            - 効率的かつ透明な権限管理が実現される

ブロックチェーン非依存のミドルウェアという位置付け
- ブロックチェーンに依存しない
    - 独自でノードを持っている
    - そのため、複数のBCやオフチェーンプラットフォーム間でのデータ読み書きが可能
        - ミドルウェア層
    - [[しきい値暗号]]技術
        - これは[[web3auth]]も同様の仕組みだった気がする<img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>
        - 秘密情報を複数の「シェア」とよばれる断片として分割し、分散させる仕組み
        - > Lit Protocolでは分散鍵生成(DKG)と呼ばれるプロセスで、公開鍵と秘密鍵のシェアを生成し、各ノードに異なるシェアを保存
            - > 生成されたECDSAのキーペアは、Lit Protocolの文脈ではProgrammable Key Pairs (PKPs)と呼ばれます。
            - ![image](https://scrapbox.io/files/6434dfb5c8d4e2001bfcd462.png)

Programmable Key Pairs（PKPs）とは
source: [Introduction | Lit Protocol Developer Docs](https://developer.litprotocol.com/pkp/intro/)
- Programmable key pair
    - Litネットワークで分散管理されるECDSAキーペア
    - Lit Actionと呼ばれるJavaScriptプログラムで指定されたアプリケーションロジックに基づき、自動的に署名するようにプログラム可能
        - ミドルウェア層としての機能
        - 自動的にTxを実行する？<img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>
        - OpenZeppelin DefenderのAutoTasks<img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>　[OpenZeppelin | Defender](https://www.openzeppelin.com/defender)
    - 各PKPは、分散鍵生成（Decentralized Key Generation）と呼ばれるプロセスを通じて、Litノードによって集合的に生成されたECDSA鍵ペアである
        - [[ECDSA]]のおさらい　[ECDSAによる署名生成と検証の仕組みを分かりやすく解説](https://zoom-blc.com/what-is-ecdsa)
    - ネットワークとして、Litは誰も秘密鍵全体を知らない状態で新しい鍵ペアを生成することができる
        - PKP NFTによって表現される
            - ownerは鍵ペアの唯一のコントローラとなる（ [/masatojames/Lit Protocol](https://scrapbox.io/masatojames/Lit Protocol)）
        - 不完全な秘密鍵から公開鍵を生成できるという意味？<img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>
    - その代わり、各ノードは鍵のシェアのみを保持
        - 単一のノードだけで鍵の利用権を持つことはできない
            - これらの署名の共有は、PKPによって署名された完全な署名を生成するために、閾値（2 of 3 of total node）以上を組み合わせる必要がある
                - 任意に定義された条件が満たされたときにtxを発行
                    - そのためにKey shareを各ノードから集約（全体の2/3）し、ファイルの複合化あるいは署名を行う<img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>
    - 署名の要求や署名ロジックの実行許可は、認可されたアクセス権を持つユーザーに限定
        - 認可されたアクセス = PKPを生成する際に使用した認証方法（ウォレット署名やoAuthトークンなど）
        - PKP NFTのowner？
- [[MPC]]設計 fyi. [/masatojames/Lit Protocol](https://scrapbox.io/masatojames/Lit Protocol)
    - [Introduction | Lit Protocol Developer Docs](https://developer.litprotocol.com/pkp/wallets/intro/)
    - ![image](https://developer.litprotocol.com/assets/images/authOverview-57c76c33650b60d3c9b14dc5bc6c8ae2.png)

SEV (Secure Encrypted Virtualization)
- セキュリティをさらに向上させるために、AMDのSEV-SNPをベアメタル実装としてノード運営者向けにハードウェアソリューションを構築

PKPの利用にEOAウォレットが必要か？
- PKPで署名するために何らかの認証方法を提示すれば良い
- [Wallet Abstraction: Google OAuth x Lit PKP](https://spark.litprotocol.com/wallet-abstraction-with-google-oauth/)
    - これもまとめる[[wallet abstraction]]

[[Lit Action]]

ユースケース
- [[Patch wallet]]
    - 実装は、ERC-4337のBundlerにLit protocolを使用している？<img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>
    - UserOp mempoolの運用も合わせて気になる
- gasless airdropper
    - [GitHub - noplan-inc/gasless-airdropper](https://github.com/noplan-inc/gasless-airdropper)
    - > ガス代無料でトークンのclaimができるサービスです。
    - >  先日開催されたFracton Hackathon Vo.1で2つの賞を獲得



