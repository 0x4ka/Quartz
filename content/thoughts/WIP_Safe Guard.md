---
title: "WIP_Safe Guard"
date: 1970-01-20T11:57:38.370Z
tags: 
---

#wallet #WalletContract

![image](https://scrapbox.io/files/644a2dfd7138c6001c53a9cb.png)

## SelfAuthorized
source: [https://github.com/safe-global/safe-contracts/blob/main/contracts/common/SelfAuthorized.sol](https://github.com/safe-global/safe-contracts/blob/main/contracts/common/SelfAuthorized.sol)
- 抽象コントラクト
- コントラクト自身でしか実行できないようなmodifierを定義

## GuradManager
source: [https://github.com/safe-global/safe-contracts/blob/main/contracts/base/GuardManager.sol](https://github.com/safe-global/safe-contracts/blob/main/contracts/base/GuardManager.sol)
- Safe.sol（singleton）に継承される抽象コントラクト
- guardの取得や設定を担う

## Singleton
source: [safe-contracts/Safe.sol at e870f514ad34cd9654c72174d6d4a839e3c6639f · safe-global/safe-contracts · GitHub](https://github.com/safe-global/safe-contracts/blob/e870f514ad34cd9654c72174d6d4a839e3c6639f/contracts/Safe.sol#L177)
- Safe Walle 本体となるコントラクト（各チェーンにたった1つだけ存在する）
- 各ユーザーごとに展開された Proxy によって呼び出される（delegateCall）
- Safe.sol（singleton）は、GuardManager.getGuard() を呼び出し、guardのコントラクトを取得する
    - その後、GuardInterfaceを実装したコントラクトの検証を実行する
        - Txを実行する前にGuard(guard).checkTransaction(...)で検証
            - 内容によってはrevertする
        - Tx実行後は、Guard(guard).checkAfterExecution(...); を実行
            - これもRevertか？
- setGuardを実行するためには、singleton自身でsetGuardを叩く必要があるため
    - singletonにGuardmanagerは展開されている


## Guard
source: [https://github.com/safe-global/safe-contracts/tree/main/contracts/examples/guards](https://github.com/safe-global/safe-contracts/tree/main/contracts/examples/guards)
- トランザクションを検査するコントラクト
- GuardManager内に記述されるInterfaceが実装される

memo
- SelfAuthorizedで実装されている modifier authorized() によって、シングルトンのみGuardを設定できる
        - setGuard(address guard) external authorized という modifier
            - 内容は、require(msg.sender == address(this), "GS031");
    - Singleton を application ごとに作成して管理するってことか！？<img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>
        - 確かにそれなら [[Safe Wallet Contract のデプロイ#6449ed1375f268000005001b]] の問題はアプリケーションごとに委ねられる
        - ちがそうだった <img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>
        - そうなるとSafeを前提にCWを開発するメリットって、別にAppSpecificなGuardをSafeの既存CWにどんどん適用できることではなくなるのか...<img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>
- GuardはCW自身で変更できてしまう
    - Guardはいわば自治だなこれ
    - 結果的に、Guardの変更には必ずSelfAuthorized()を通る必要があるため、必ずexecTransaction()を通る
        - Module で bypass 可能なので規制が必要
    - ![image](https://scrapbox.io/files/6469d1035bcb09001c6ea976.png)

- もはやSafeに提案するしかないか？<img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>
    - アプリケーションを承認して、Guard のロジックを変更してもらう
    - このとき、CW Owner は Guardのロジックを変更することはできない
        - 必ずアプリケーションを通して解除してもらう必要がある。みたいな機構を作りたい
            - 適用されるModule全体にGuardによるcheckTransaction()が走るようなGlobalなコンセプトが必要
                - [[safe の module は権限分離を主眼としている]]
    - GuardではなくBlockerとか Limitterとかになりそう


しんぎ
- SelfAuthorizedを含む、`setGuard()`実行に関する図解
![image](https://scrapbox.io/files/646352323bd8d0001c46ea4f.png)

