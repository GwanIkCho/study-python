# McZlCSJqmptup_XgvTzr
# mS96wHyYc5
# https://openapi.naver.com/v1/papago/n2mt

import urllib.request
import json

client_id = 'McZlCSJqmptup_XgvTzr'
client_secret = 'mS96wHyYc5'
encodings_text = urllib.parse.quote('둠-황-챠')
data = f'source=ko&target=en&text={encodings_text}'
url = 'https://openapi.naver.com/v1/papago/n2mt'
request = urllib.request.Request(url)

request.add_header('X-Naver-Client-Id', client_id)
request.add_header('X-Naver-Client-Secret', client_secret)
response =urllib.request.urlopen(request, data=data.encode('utf-8'))
rescode = response.getcode()

if rescode == 200:
    response=json.loads(response.read().decode('utf-8'))
    print(response['message']['result']['translatedText'])