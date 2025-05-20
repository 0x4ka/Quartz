---
title: Following ERC-6900 discussions
date: 1970-01-20T11:51:54.017Z
tags: 
---

#WalletContract #wallet
source: [ERC-6900: Modular Smart Contract Accounts and Plugins - EIPs - Fellowship of Ethereum Magicians](https://ethereum-magicians.org/t/erc-6900-modular-smart-contract-accounts-and-plugins/13885)

登場人物
- [adamegyed](https://ethereum-magicians.org/u/adamegyed) author from alchemy
- [trinity-0111](https://ethereum-magicians.org/u/trinity-0111) author from alchemy
- [fmc](https://ethereum-magicians.org/u/fmc) filip at biconomy
- [jamesmccomish](https://ethereum-magicians.org/u/jamesmccomish) unknown [twitter](https://twitter.com/james_mccomish)

- Validation plugins


some private img below
![image](https://scrapbox.io/files/6460819284e03b001c665923.png)
![image](https://scrapbox.io/files/6460819b47aac9001b0e9c9b.png)
![image](https://scrapbox.io/files/646081a3f558d6001c71d893.png)
![image](https://scrapbox.io/files/646081b5d0ddad001b7c64f7.png)

reference link:
- Smart Contracts
    - [Smart Account](https://github.com/bcnmy/scw-contracts/blob/Ownerless-SA-Auth-Modules-hardhat-deploy/contracts/smart-contract-wallet/SmartAccount.sol)
    - [Sample EOA Ownership Authorization Module](https://github.com/bcnmy/scw-contracts/blob/Ownerless-SA-Auth-Modules-hardhat-deploy/contracts/smart-contract-wallet/modules/EOAOwnershipRegistryModule.sol)
    - [Smart Account Factory](https://github.com/bcnmy/scw-contracts/blob/Ownerless-SA-Auth-Modules-hardhat-deploy/contracts/smart-contract-wallet/SmartAccountFactory.sol)
- Tests cases
    - [Executing userOps, EIP1271 and Forward Transactions with ownerless SA’s](https://github.com/bcnmy/scw-contracts/blob/Ownerless-SA-Auth-Modules-hardhat-deploy/test/smart-account/SA-Basics.specs.ts)
    - [How to upgrade Biconomy SA v1 to Ownerless SA](https://github.com/bcnmy/scw-contracts/blob/Ownerless-SA-Auth-Modules-hardhat-deploy/test/upgrades/v1-to-v2/v1-to-v2-upgrade.specs.ts)

