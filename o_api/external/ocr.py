# https://ocr.space/OCRAPI
# K83131551288957
# https://api.ocr.space/parse/imageurl?apikey=&url=


url = 'https://api.ocr.space/parse/imageurl?apikey=K83131551288957&url=https://i.pinimg.com/474x/34/8b/c5/348bc51a10af4a96dea207318f88cc6b.jpg&language=kor&isOverlayRequired=true'

import requests

response = requests.get(url)
response.raise_for_status()
result = response.json()
print(result['ParsedResults'][0]['ParsedText'])