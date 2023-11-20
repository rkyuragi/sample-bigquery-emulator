# sample-bigquery-emulator

下記参考サイトでやっていることをGitHubに登録しただけ

[参考サイト](https://qiita.com/Hisaaki-Kato/items/7b57e53058d80b71c8c0)

## 構築&データ挿入

```shell
$ docker-compose build --no-cache
$ docker-compose up -d
```

## データ取得

```shell
$ docker-compose exec app python main.py
Row((1, 'alice'), {'id': 0, 'name': 1})
Row((2, 'bob'), {'id': 0, 'name': 1})
```

## 終了

```shell
$ docker-compose down
```
