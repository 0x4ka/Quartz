# Biconomy Smart Contract Wallet

作成日時: 2023-05-08 08:50:25
更新日時: 2024-08-16 07:19:49

Biconomy Smart Contract Wallet
#wallet #WalletContract
source: https://github.com/bcnmy/scw-contracts
doc: https://docs.biconomy.io/additional-content/smart-contract-wallets

 [ERC-4337] に準拠した SCW
 機能
 	[Multi-signature]
 	Daily transaction amount limit
 	Batch transactions
 Architecture
 	Proxy pattern
 		ユーザの具体的な資産は `Proxy.sol` に格納される
 	Smart Account
 		[ERC-4337] をベースに前述した機能を実装しているロジックコントラクト
 		... 本当か？[taxio.icon]
 			SmartAccountFactory があるし、SmartAccount 内にも owner が定義されているので、もしかしたらUser 毎に deploy することを想定しているのかもしれない[taxio.icon]]
 			deploy コストがすごいことになりそうだけど[taxio.icon]

 BiconomyのSmartAccount.solにはGuardによるTx検証機構が含まれてない
 	AAの実装的に無理なのかな[0xhid3.icon]
 	GuardManager.sol自体はrepoに存在してるけど、どこにも継承されてない 	[Safeの実装 https://github.com/safe-global/safe-contracts/blob/7a77545f288361893313af23194988731ee95261/contracts/Safe.sol#L139]　[Biconomyの実装 https://github.com/bcnmy/scw-contracts/blob/6b4d3b71c3621c2d171343e38c27ef46e5bed6be/contracts/smart-contract-wallet/SmartAccount.sol#L245]
 	

