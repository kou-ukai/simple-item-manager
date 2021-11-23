# training-flask
FlaskとVue3で勉強がてら何か開発するリポジトリです。

## 要件
- Web NFCを使ってパスワードなしでログインする何か
- ログインしてどうしよう

## 環境構築
VSCodeの拡張機能「Remote - Containter」を使ってDockerコンテナ内で開発することを前提としています。
コンテナ初期回作成後にパッケージやモジュールをインストールする必要があります。
コンテナを再作成した場合、再度インストールしてください。
### サーバ
```pip3 install --no-cache-dir -r requirements.txt```
### クライアント
```npm install```
