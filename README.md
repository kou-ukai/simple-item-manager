# simple-item-manager
FlaskとVue3で勉強がてら何か開発するリポジトリです。

## 要件
- 物品利用者管理システム
- NFCを読み取ってパスワードなしでログインできる
- QRコードを読込んで物品を検索できる

## 環境構築
VSCodeの拡張機能「Remote - Containter」を使ってDockerコンテナ内で開発することを前提としています。
コンテナ初期回作成後にパッケージやモジュールをインストールする必要があります。
コンテナを再作成した場合、再度インストールしてください。
### サーバ
```pip3 install --no-cache-dir -r requirements.txt```
### クライアント
```npm install```
