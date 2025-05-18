# EOAをmultichainIDとして扱う

作成日時: 2024-03-30 05:35:27
更新日時: 2024-03-30 06:05:38

EOAをmultichainIDとして扱う
#MultichainID #WalletContract #wallet

ref: https://ethereum-magicians.org/t/chain-specific-addresses/6449


複数のコントラクトウォレットに対して、単一のeoaが操作権限を持ち
ソーシャルリカバリーの余地を与える
eoaはIDとして機能する

EOAの作成をソーシャルアカウントで実装
　key management: MPC
EOA→ENS subdomainの提供
　プロパティに各チェーンのAAウォレットを紐付け（[MultichainID]）


