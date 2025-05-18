# Scrapboxの中身を自動ツイートする

作成日時: 2023-04-06 06:08:15
更新日時: 2023-04-06 06:13:12

Scrapboxの中身を自動ツイートする
要件
　Scrapboxのコンテンツを定期的に自動でツイートしたい
　　gasのスケジューラでいけそう
　分量が多い時はスレッド化
　　TwitterAPIを読む
　GASとスプシでTwitterIDと Scrapbox、支払いなどを管理したい
　 これは上が整理できたらいけそう

以下の方法でGASからスレッド投稿はできそう
https://www.noelcafe.com/blog/entry_010156/

Scrapboxの内容を取得する方法
　XMLpathで行ける気がする
　Scrapboxは編集すると内容が変わるのでその辺がpathに影響するか要確認




