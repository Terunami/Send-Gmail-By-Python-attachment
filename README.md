# Send-Gmail-By-Python-attachment
Send-Gmail-Python revenge with attachment

参考リンク：
    ・https://qiita.com/ekzemplaro/items/29be7ed72497ba85d8dc
    ・https://www.it-swarm.dev/ja/python/importerror%EF%BC%9Aapiclientdiscovery%E3%81%A8%E3%81%84%E3%81%86%E5%90%8D%E5%89%8D%E3%81%AE%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB%E3%81%AF%E3%81%82%E3%82%8A%E3%81%BE%E3%81%9B%E3%82%93/1040346249/


・主な追加点
    1. 複数のファイル添付を追加
        file_attch の文字列型変数を file_attach_list のリスト型変数に変更
        attachment_message() にてループ処理による添付に変更

    2. BB, BCC の追加
        message['Cc'], message['Bcc'] への代入を追加

・使い方
    準備
        1. credentials.py を同ディレクトリに配置。（取得の仕方は検索して）
        2. pip install -r requirements.txt  を実行してパッケージを揃える。

    送信
        1. test_gmail.py を編集して送信するメールの情報を編集。
        2. (初めての場合、)　python test_gmail.py --noauth_local_webserver　を実行。
           アプリを認証する。(細かい手順は検索して)
           ２回目以降は python test_gmail.py で実行。

・メモ
     TO CC,BCC を複数指定する場合は、 "アドレス1;アドレス2;アドレス3" のように ; で区切る。
     添付ファイルは、絶対パスでも相対パスでもOK.