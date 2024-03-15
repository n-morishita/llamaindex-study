## コンテナの作成

### 以下のコマンドを実行してコンテナを起動する

```
cd docker
docker-compose up -d
```

### 一度コンテナを削除し、再度作成する場合

```
docker-compose build --no-cache
docker-compose up -d
```

## アプリの実行

作成したコンテナの Exec で以下のコマンドを実行

```
python3 main.py
```

## モジュールのインストール

作成したコンテナの Exec で pip install を実行
