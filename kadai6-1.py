import requests
# APIエンドポイント
# https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData

APP_ID = "6810530fe3685d18b2c5fc59ecb8eb8aa7a94ca6"  # ここに自分のAPIキーを入れる

API_URL = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId": "0003142449",    # 毎月勤労統計調査 詳細集計の統計データID
    "metaGetFlg": "Y",              # メタ情報取得（変数名やラベルなど）
    "cntGetFlg": "N",               # 件数取得しない
    "explanationGetFlg": "Y",       # 統計の説明情報を取得
    "annotationGetFlg": "Y",        # 注釈情報も取得
    "sectionHeaderFlg": "1",        # セクションヘッダーを取得
    "replaceSpChars": "0",          # 特殊文字を置換しない
    "lang": "J"                     # 日本語で取得
}

# APIにGETリクエストを送る
response = requests.get(API_URL, params=params)

# レスポンスのJSONを辞書型に変換
data = response.json()

# APIから取得した生データをそのまま表示
print(data)

