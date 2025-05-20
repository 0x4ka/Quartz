---
title: 'Ownerless Smart Account Architecture'
date: 2023-05-14T06:38:53.000+09:00
tags: 
---

![image](https://scrapbox.io/files/6460819284e03b001c665923.png)
![image](https://scrapbox.io/files/6460819b47aac9001b0e9c9b.png)
![image](https://scrapbox.io/files/646081a3f558d6001c71d893.png)
![image](https://scrapbox.io/files/646081b5d0ddad001b7c64f7.png)

Smart Contracts
Smart Account: [https://github.com/bcnmy/scw-contracts/blob/Ownerless-SA-Auth-Modules-hardhat-deploy/contracts/smart-contract-wallet/SmartAccount.sol](https://github.com/bcnmy/scw-contracts/blob/Ownerless-SA-Auth-Modules-hardhat-deploy/contracts/smart-contract-wallet/SmartAccount.sol)
Sample EOA Ownership Authorization Module: [https://github.com/bcnmy/scw-contracts/blob/Ownerless-SA-Auth-Modules-hardhat-deploy/contracts/smart-contract-wallet/modules/EOAOwnershipRegistryModule.sol](https://github.com/bcnmy/scw-contracts/blob/Ownerless-SA-Auth-Modules-hardhat-deploy/contracts/smart-contract-wallet/modules/EOAOwnershipRegistryModule.sol)
Smart Account Factory: [https://github.com/bcnmy/scw-contracts/blob/Ownerless-SA-Auth-Modules-hardhat-deploy/contracts/smart-contract-wallet/SmartAccountFactory.sol](https://github.com/bcnmy/scw-contracts/blob/Ownerless-SA-Auth-Modules-hardhat-deploy/contracts/smart-contract-wallet/SmartAccountFactory.sol)
Tests cases
Executing userOps, EIP1271 and Forward Transactions with ownerless SA’s: [https://github.com/bcnmy/scw-contracts/blob/Ownerless-SA-Auth-Modules-hardhat-deploy/test/smart-account/SA-Basics.specs.ts](https://github.com/bcnmy/scw-contracts/blob/Ownerless-SA-Auth-Modules-hardhat-deploy/test/smart-account/SA-Basics.specs.ts)
How to upgrade Biconomy SA v1 to Ownerless SA: [https://github.com/bcnmy/scw-contracts/blob/Ownerless-SA-Auth-Modules-hardhat-deploy/test/upgrades/v1-to-v2/v1-to-v2-upgrade.specs.ts](https://github.com/bcnmy/scw-contracts/blob/Ownerless-SA-Auth-Modules-hardhat-deploy/test/upgrades/v1-to-v2/v1-to-v2-upgrade.specs.ts)
