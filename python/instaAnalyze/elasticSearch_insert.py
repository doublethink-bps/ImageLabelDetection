from elasticsearch import Elasticsearch
import os

def elastic_insert(labels,posttime):
    elastic_password=os.environ['ELASTIC_PASSEWORD']
    #Elasticsearch に接続
    es = Elasticsearch(
        "https://[ELASTIC_IPADDRESS or HOSTNAME]:9200",
        ca_certs=os.environ['CA_CERTS_ELASTIC'],
        basic_auth=("elastic",elastic_password)
    )
    #取得したラベルを挿入
    for label in labels:
        document = {
            "imagetag": label.description,
            "@timestamp":posttime
        }
        try:
            es.index(index='testindex01',document=document)
        except es.ApiError as e:
            print(e)
    #Elasticsearch から切断
    es.close()