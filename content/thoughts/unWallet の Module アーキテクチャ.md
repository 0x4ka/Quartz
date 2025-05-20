---
title: unWallet の Module アーキテクチャ
date: 1970-01-20T11:40:12.591Z
tags: 
---

#WalletContract #wallet
[https://sivira.co/assets/pdf/unWallet_Contract_Design.pdf](https://sivira.co/assets/pdf/unWallet_Contract_Design.pdf)
[https://github.com/SIVIRA/unwallet-contracts/tree/master](https://github.com/SIVIRA/unwallet-contracts/tree/master)

![image](https://scrapbox.io/files/645766f8af80400872e77d3f.png)

- ModuleManager と ModuleRegistry は別でデプロイする
    - ModuleManger の初期値として ModuleRegistry を追加
        - ModuleRegistryにmoduleの有効/無効を保存していると思ったけど、Managerコントラクトにも同じマッピング変数が定義されている
        - もしかすると ModuleRegistry は 第三者によって一括管理されている可能性がある
            - つまり、ModuleRegistryに追加されたモジュールだけが、Managerを通して登録できる
            - モジュールの信頼性を担保する役割を充てようとしている
 moduleManager.sol

```
function enableModule(address module) external override onlyOwner {
        require(!_modules[module], "MM: module is already enabled");
        require(
            _registry.isModuleRegistered(module),
            "MM: module must be registered"
        );

        _modules[module] = true;

        emit ModuleEnabled(module);
    }
```

