import requests

#参照したオープンデータ: OMDb API (Open Movie Database)
#映画やテレビ番組の情報を提供するAPI
#エンドポイント:
#  - http://www.omdbapi.com/
#映画タイトルによる検索
#タイトル検索は`t`パラメータにタイトル文字列を指定。

OMDB_API_URL = "http://www.omdbapi.com/"
params = {
    "apikey": "1be8041a",
    "t": "Inception"   # ここを好きな映画タイトルに変更可能
}
response = requests.get(OMDB_API_URL, params=params)
data = response.json()

print(data)
