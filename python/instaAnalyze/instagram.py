import requests
import json
import os
import urllib.error
import urllib.request
import visonLabel
from dateutil import tz,parser
import elasticSearch_insert


#環境変数からアクセストークン取得
accessToken=os.environ["ACCESSTOKEN"]
userid=os.environ["INSTAGRAM_USER_ID"]

#インスタ投稿画像リストID取得先エンドポイント
medialist_endpoint="https://graph.instagram.com/v16.0/{userid}/media".format(userid=userid)
params={
    'access_token':accessToken
}
#インスタ投稿画像リスト取得
res = requests.get(medialist_endpoint,params=params)
data = json.loads(res.text)
#最後に投稿した画像リストのID
media_id=data["data"][0]["id"]

#画像URL取得先エンドポイント
mediaurl_endpoint="https://graph.instagram.com/{media_id}".format(media_id=media_id)
params={
    'fields':'id,media_type,media_url,timestamp',
    'access_token':accessToken
}
#画像URL取得
res = requests.get(mediaurl_endpoint,params=params)
data = json.loads(res.text)
MEDIAURL = data['media_url']
#画像投稿時間取得
TIMESTAMP = data['timestamp']
dt_naive = parser.parse(TIMESTAMP)
dt_aware = dt_naive.astimezone(tz.gettz('Asia/Tokyo'))

dst_url = os.getcwd()+"/insta_post.png"

#画像の保存
try:
    with urllib.request.urlopen(MEDIAURL) as web_file:
        data = web_file.read()
        with open(dst_url,mode='wb') as local_file:
            local_file.write(data)
except urllib.error.URLError as e:
    print(e)

#保存した画像のラベル分析
labels = visonLabel.visonImageLabelDetection(dst_url)
elasticSearch_insert.elastic_insert(labels,dt_aware)
