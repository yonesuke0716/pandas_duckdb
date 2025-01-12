# pandas_duckdb
pandasをduckdbと併用して高速化を試すデモアプリ

## Docker準備
- Dockerイメージのビルド（初回のみ）
```
docker build -t pandas_duckdb .
```

- コンテナの起動
```
docker compose up -d
```

- 実行
```
docker exec -it pandas_duckdb bash
```

## ダミーデータの作成
以下のコマンドでデモに必要なダミーデータを作成する。
```
python dataset.py
```

## Streamlitアプリの起動
ダミーデータが作成できたら、pandas、duckdbそれぞれのStreamlitアプリを起動する。
```
streamlit run pandas_base.py
or
streamlit run duckdb_base.py
```

- 終了
```
exit
docker compose down
```


## 参考

### Python Example
https://github.com/duckdb/duckdb/blob/main/examples/python/duckdb-python.py