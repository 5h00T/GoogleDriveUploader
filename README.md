# GoogleDriveUploader
GoogleDriveに指定したディレクトリ以下の全てのファイルとフォルダをアップロードする
### 準備
`pip install google-api-python-client PyDrive` 必要なライブラリをインストール
https://developers.google.com/drive/v3/web/quickstart/python の通りにAPIを利用する準備をする<br>
client_secrets.jsonを同じフォルダ内に置く

### 実行
`python upload.py フォルダの名前`<br>
それ以下のフォルダがアップロードされる
