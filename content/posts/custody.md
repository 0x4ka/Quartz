---
title: "custody"
date: "1970-01-20T12:07:44.807Z"
tags:
  
---

- Safe basis
    - deploy for each users
        - 初期費用（3000円 ~ 5000円）
        - 月額費用（1000円/NFT）
    - Multi-sig
        - 1 is end-user
        - 3 are synschismo EOA
            - EOA - metamask
            - HWW - Ledger
            - CW - Argent (for ethereum)
            - MPC - Web3auth (little risky)
        - threshold: 3/4
    - end-user can:
        - connect wallet to dapp
            - so that user can claim allowlist/claim NFT
        - execute Tx without transfer() / approve()
            - whitelist for enduser's Tx
    - Data table:
        - end-user's eKYC data
            - generate sign with contract wallet which enduser has.
            - store sign bytescode in enduser's contract wallet
        - contract wallet address
            - collation enduser's eKYCdata and encoding hash witch hased by contract wallet signature


