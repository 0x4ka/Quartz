# Avocado Wallet のソースコード

作成日時: 2023-05-01 21:48:51
更新日時: 2023-05-07 02:56:29

Avocado Wallet のソースコード
#wallet #WalletContract

Avocado wallet の特徴であるabstractionについては別途参照
 [gas abstraction]
 [Network abstractionの重要性]
 [Account Abstraction Architecture]

Avocado wallet の activity は dune analytics で確認
　https://dune.com/murathan/avocado-wallet
　https://dune.com/murathan/avocado-wallet-top-assets-and-top-wallets

[** AvoSafe]
https://etherscan.io/address/0x66767ba0fdd48ca144ef304405c1a5dbb842e75f#code
  - AvoSafeはAvoWalletのProxyとして機能する
  fallback関数が呼び出されると、ストレージからAVOWalletImplコントラクトのアドレスを読み込む
  コールデータの先頭4バイトが "_avoWalletImpl()"関数のシグネチャであるかどうかを確認する
  "_avoWalletImpl()"関数のシグネチャである場合、AVOWalletImplコントラクトのアドレスを返す
  上記以外の場合、AVOWalletImplコントラクトにコールデータを転送する
  AVOWalletImplコントラクトの実行結果を返す
 Safeのコントラクトをベースにしている

[** AvoFactoryProxy]
https://etherscan.io/address/0x3adae9699029ab2953f607ae1f62372681d35978#code
 Identifier Proxy としての AvoSafe をデプロイするための factory

[** AvoFactory]
https://etherscan.io/address/0x77f193818a3f7a1d01e75c16c9083fc4001908f4#code
 AvoFactoryProxyのimprementation contract
 import（主要）
 	AvoSafe
  IAvoWalletV2
  IAvoVersionsRegistry
  IAvoFactory
  IAvoForwarder

[** AvoWallet]
https://etherscan.io/address/0x3718f4bf9140f333bca79Cb279F09f0bB8E6dDEE#code
 おそらく AvoSafe が呼び出す AvoWallet の singleton
 Instadapp Flashloan Aggregator が使用するコールバックがwallet本体に定義されてた
 	FLASHLOAN CALLBACK (L:242) 
 	Flashloan された金額を所有しながらオペレーションを実行する
 		つまり aave で flashloan() を実行した際に、aave contract からCallbackを受け、さらに目的のDeFiプロトコルのTxを実行するためのCallback関数を実装している
 import（主要）
 	IAvoWalletV2
  IAvoVersionsRegistry
  InstaFlashReceiverInterface

