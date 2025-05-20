---
title: Pinky Protocol
date: 1970-01-20T11:50:18.009Z
tags: 
---

#wallet
source: [https://ethglobal.com/showcase/pinky-protocol-vsos2](https://ethglobal.com/showcase/pinky-protocol-vsos2)

- Guard内部の`checkTransfer()`メソッドでguardの適用を外されないように規定してる
 solidity.js

```javascript
function checkTransaction(
        address to,
        uint256 value,
        bytes memory data,
        Enum.Operation operation,
        uint256 safeTxGas,
        uint256 baseGas,
        uint256 gasPrice,
        address gasToken,
        address payable refundReceiver,
        bytes memory signatures,
        address msgSender
    ) external override {
        // User cannot set approval for borrowed tokens
        require(!IsApproval(data), "You are not allowed to set approval for token");
        // User cannot setup another guard
        require(!IsSetGuard(data), "You are not allowed to setup another guard");
    }
```

    - これ行けるのを知らなかった
        - つまり、`setGuard()`を実行する場合は、必ずトランザクションが検証されるっていうことか？
solidity.js

```javascript
function IsSetGuard(bytes memory data) internal pure returns (bool) {
        bytes4 ExpectedSetGuardFunctionSelector = bytes4(keccak256("setGuard(address)"));

        // If transaction data is shorter than 4 bytes it is not a setGuard transaction
        if (data.length < 4) {
            return false;
        }

        // Get the function selector
        bytes4 ActualFunctionSelector;
        assembly {
            ActualFunctionSelector := mload(add(data, 32))
        }

        // Check if function selector corresponds to the setGuard function
        return ActualFunctionSelector == ExpectedSetGuardFunctionSelector;
    }
```

    - `isSetGuard()`メソッドの内部で、setGuardのメソッドをcallしているかどうかを検証している

- GuardManager.solには以下のコントラクトが含まれている
    - interface : Gurad
    - abstract : BaseGuard（Guardを継承している）
    - abstract : GuradManager

- PinkyのGuardで利用しているのは限定的かも
    - BaseGuard と Guard
        - checkTransactionとcheckAfterExecutionのインターフェースとsupportsInterfaceのみ
    - GuardManagerは継承していない
        - Safe.solが継承しているので、GuardManagerは結構利用主体が異なるコントラクトをひとまとめにされてる印象
        - ややこしー<img src='https://scrapbox.io/api/pages/0xhid3-private/0xhid3/icon' alt='0xhid3.icon' height="19.5"/>

