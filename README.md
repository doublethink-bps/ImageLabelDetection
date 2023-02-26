# ImageLabelDetection

インスタグラムに投稿した画像のラベル検出が出来ます。  
検出したラベルはElasticSearchに保存し、kibanaでグラフ化できるようにします。

## 1.準備

インスタグラムのアクセストークン、googleのCloudVisonAIとElasticsearch の準備が必要です。  
以下を参照して、準備します。

・インスタのアクセストークン取得方法  
https://developers.facebook.com/docs/instagram-basic-display-api/getting-started

・GoogleCloudVisonAIアクセスキーを取得  
https://cloud.google.com/vision/docs/detect-labels-image-client-libraries?hl=ja#client-libraries-usage-python

・ElasticSearchの準備  
https://qiita.com/charatech_bps/items/40966d9d53c2789ee412

続いて環境変数を設定します。
```
export ACCESSTOKEN = <instagramのトークン>  
export INSTAGRAM_USER_ID = <instagramのユーザID>  
export ELASTIC_PASSEWORD = <Elasticsearchのelasticユーザのパスワード>  
export CA_CERTS_ELASTIC = <ElasticsearchのSSL証明書の保存先パス>  
export GOOGLE_APPLICATION_CREDENTIALS = <GoogleCloudのVisonAPIを使用するためのアクセスキー保存先絶対パス>  
```

## 2.実行

elasticSearch_insert.pyから、elasticsearchが構築されたサーバのIPまたはホスト名を設定します。

```elasticSearch_insert.py
    es = Elasticsearch(
        "https://[ELASTIC_IPADDRESS or HOSTNAME]:9200",　←　ここの[ELASTIC_IPADDRESS or HOSTNAME]を変更
        ca_certs=os.environ['CA_CERTS_ELASTIC'],
        basic_auth=("elastic",elastic_password)
    )
```

instagram.pyを実行すると、インスタグラムに最終投稿した画像のラベル検出が実行され、Elasticsearch に  
投稿日時とラベルを保存していきます。
```
python3 instagram.py
```

## 3.実行結果

正常に実行されるとコンソール上何も戻ってきませんが、
Elasticsearchにはラベルが保存されます。  
保存されたら、kibanaでグラフの設定をして、期間を設定し、投稿した画像から検出したラベルと検出数などを表示させることが出来ます。  

![image](https://user-images.githubusercontent.com/126371575/221403088-13714c22-dd58-4c5a-a7d6-991a564b97d6.png)






