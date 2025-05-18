# 既存の Contract Wallet にwrite操作を禁止するモジュールを加えても被Approvalユーザーにバイパスされ得る

作成日時: 2023-06-17 22:13:02
更新日時: 2023-06-18 11:26:05

既存の Contract Wallet にwrite操作を禁止するモジュールを加えても被Approvalユーザーにバイパスされ得る
#WalletContract #wallet

 ERC721等のトークン規格では、write権限を委譲する`setApprovalForAll()`が存在する
 上記メソッドは、`mapping(address => mapping(address => bool))` で保持されるため委譲先をオンチェーンからリスト形式で取得できない
 	過去のtransaction, eventログをblockchain explorer等を使って炙り出し、該当する全ての委譲先についてbool値をFALSEに変更させる必要がある
 		委譲先の数だけ、ストレージの書き込みに対するガス代がかかる

[* 結論: トラストポイントが発生するし、運用コストから見ても非現実的]

