# Safe Wallet Contract のデプロイ

作成日時: 2023-04-26 23:33:40
更新日時: 2023-04-27 05:21:27

Safe Wallet Contract のデプロイ
#Wallet #WalletContract

Overview
 [Proxy Factory https://polygonscan.com/address/0xa6b71e26c5e0845f74c812102ca7114b6a896ab2] によって [Proxy https://polygonscan.com/address/0xC31823f15F32A99Cd9Cd9F1b88bad8463e750C9B#code] が各ユーザーをOwnerとしてデプロイされる
 	Proxy は唯一のウォレットコントラクト[Singleton https://polygonscan.com/address/0x3E5c63644E683549055b9Be8653de26E0B4CD36E#code] をdelegateCallする
![644a2a0d7ac9ce001b1b86e2.png](./img/644a2a0d7ac9ce001b1b86e2.png)

Detail
　Safeが管理するwalletのコントラクトは、ProxyFactory.createProxyWithNonce()の引数singletonとして指定される
　　ProxyFactory.deployProxy()内で、Proxyのバイトコードを呼び出しデプロイしている
　　　バイトコードの呼び出しは type(SafeProxy).creationCode を用いている
　　　	>コントラクトのバイトコードの生成を含んでいるメモリーバイト配列 カスタムクリエーションルーティンを作るためにインラインアッセンブリで使用できます
    >source: [Units and Globally Available Variables — Solidity 0.5.4 ドキュメント](https://solidity-jp.readthedocs.io/ja/latest/units-and-global-variables.html#type-information)(https://solidity-jp.readthedocs.io/ja/latest/units-and-global-variables.html#type-information Units and Globally Available Variables — Solidity 0.5.4 ドキュメント)
 　　　　[proxyCreationCode https://polygonscan.com/address/0xa6b71e26c5e0845f74c812102ca7114b6a896ab2#readContract#F1]
　　Singletonとは
　　	Safeがデプロイした各バージョン唯一のウォレットコントラクト
　　		>シングルトンとは、オブジェクト指向プログラミングにおけるクラスのデザインパターンの一つで、実行時にそのクラスのインスタンスが必ず単一になるよう設計すること。
    > source: https://e-words.jp/w/シングルトン.html
    	![644a32f32aeee8001ce3824c.png](./img/644a32f32aeee8001ce3824c.png)
　　	Safeによって厳密に管理されるべき
　　		トラストポイントではある（ウォレット生成時にSingletonのアドレスと実装を確認できる?[0xhid3.icon]）
　　		Singletonがアップデートされることってあるのか？
　　			ユーザーが自分で切り替える？
　　deployProxyによってsingletonでInitializeされたProxyが各ユーザーに割り当てられる
　　	[safe-contracts/SafeProxy.sol at e870f514ad34cd9654c72174d6d4a839e3c6639f · safe-global/safe-contracts · GitHub](https://github.com/safe-global/safe-contracts/blob/e870f514ad34cd9654c72174d6d4a839e3c6639f/contracts/proxies/SafeProxy.sol)(https://github.com/safe-global/safe-contracts/blob/e870f514ad34cd9654c72174d6d4a839e3c6639f/contracts/proxies/SafeProxy.sol safe-contracts/SafeProxy.sol at e870f514ad34cd9654c72174d6d4a839e3c6639f · safe-global/safe-contracts · GitHub)
　　	proxyが正しいsingletonを参照しているかは、fallback関数にmasterCopy()のバイトコードを渡すと確認できる
　　	fallbackを呼び出すときにdataとして以下の値を渡すとsingletonの値が返ってくる。
　　		>// 0xa619486e == keccak("masterCopy()"). The value is right padded to 32-bytes with 0s
    > 0xa619486e00000000000000000000000000000000000000000000000000000000
    これで、CWがSafeが想定する実装になっているか確認できるわけか。
    	fallback関数の戻り値だけ変えてあげれば偽装できちゃう？
   	それ以外の場合は、singletonアドレスに対してdelegatecallを行う。
   		凄過ぎ[0xhid3.icon]
   コントラクトウォレットのデプロイコストが極限まで下げられている
   	全体で163行のみ
　https://polygonscan.com/tx/0xa8e53f17b5b5173d3aa39e922a3a536c8bb6dbfc7bd7e430af59351b4260952a
　https://github.com/safe-global/safe-contracts/blob/main/contracts/proxies/SafeProxyFactory.sol
