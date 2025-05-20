---
title: "ERC-1271: Standard Signature Validation Method for Contracts"
date: "1970-01-20T11:35:02.326Z"
tags:
  
---

#wallet
[https://eips.ethereum.org/EIPS/eip-1271](https://eips.ethereum.org/EIPS/eip-1271)

- 2018-7-25に作成されている

## summary
- EOAは秘密鍵によってメッセージに署名できるがコントラクトアカウント（CA）はできない
- dappsやコントラクトには、特定の署名によってしか実行できないものが多く、CAがEOAのように振る舞う仕組みが必要
- CAを保有するEOAによって署名を代理する必要があるため、代理署名が有効化検証する標準的な仕様を提案している

## motivation
- 複数人でのasset管理においてmulti-sig walletの活用やAAの進展など、将来的にCWが増えていく
- CWで、onlyOwner等の特定の署名を求められるコントラクトを実行できるようになる

## Code
 solidity.js

```javascript
pragma solidity ^0.5.0;

contract ERC1271 {

  // bytes4(keccak256("isValidSignature(bytes32,bytes)")
  bytes4 constant internal MAGICVALUE = 0x1626ba7e;

  /**
   * @dev Should return whether the signature provided is valid for the provided hash
   * @param _hash      Hash of the data to be signed
   * @param _signature Signature byte array associated with _hash
   *
   * MUST return the bytes4 magic value 0x1626ba7e when function passes.
   * MUST NOT modify state (using STATICCALL for solc < 0.5, view modifier for solc > 0.5)
   * MUST allow external calls
   */ 
  function isValidSignature(
    bytes32 _hash, 
    bytes memory _signature)
    public
    view 
    returns (bytes4 magicValue);
}
```


