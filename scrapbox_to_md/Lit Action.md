# Lit Action

作成日時: 2023-05-04 13:48:39
更新日時: 2024-02-06 21:43:48

Lit Action
#WalletContract
source: [/masatojames/Lit Protocol#64321d285beced0000af74ba]

  - Lit Protocol独自のスマートコントラクト
    - 実態はIPFSに保存された不変のJavaScriptのコード
    - Litの閾値暗号ネットワーク上で実行されるJavaScript関数。JavaScriptのスマートコントラクトであり、PKPと組み合わせることで、取引やその他の任意のデータに署名するようにプログラムすることができます
    - >[_* 実現できる制御の例]
  > 「n以上のEtherを保有していること」というオンチェーン条件を満たすユーザーにのみ暗号化された静的コンテンツの復号鍵を提供する
  > 「ユーザーはNFTを保有していること」といったオンチェーン条件を満たしたユーザーにのみ、署名を提供する。
  > Google OAuth、Discordなどのオフチェーンサービスの認証情報をみて、オンチェーン取引を実行する
