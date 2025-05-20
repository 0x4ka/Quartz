---
title: "Safe Module"
date: 1970-01-20T11:27:29.142Z
tags: 
---

#wallet #WalletContract

source: [safe-contracts/ModuleManager.sol at main · safe-global/safe-contracts · GitHub](https://github.com/safe-global/safe-contracts/blob/main/contracts/base/ModuleManager.sol)

- ユーザーが任意のfunctionを実装し、第三者に提供できる
    - Openseaのfilterer operator の registry にちかい使用感
        - サブスクして利用する
- Moduleはあくまでも標準のexecuteメソッドを叩く代わりにModuleを通して叩くこともできるという選択肢を提供するに限る
    - `execTransactionFromModule()`
    - `mapping(address => address) internal modules;` とあるように、ウォレットに対してモジュールはN個存在する
        - `enableModule()`と`disableModule()`でモジュールの脱着を行う
            - `authorized` modifierがあるようにこれは Proxy コントラクトを通してのみ実行可能
    - ⇄ [[WIP_Safe Guard]] はTx実行の前後に検証を行う

- Module のセットアップ
 ModuleManager.sol

```
function setupModules(address to, bytes memory data) internal {
        require(modules[SENTINEL_MODULES] == address(0), "GS100");
        modules[SENTINEL_MODULES] = SENTINEL_MODULES;
        if (to != address(0)) {
            require(isContract(to), "GS002");
            // Setup has to complete successfully or transaction fails.
            require(execute(to, 0, data, Enum.Operation.DelegateCall, gasleft()), "GS000");
            // ここの data に Module の内容を書き込んでる？
        }
    }
```

