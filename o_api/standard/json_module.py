# dick 는 데이터 교환을 이용해서 사용합니다.

import json

data = {'name' : "책", 'print': 25_000, 'stock': 55 }
print(data)

# dick를 json으로 변환
# ensure_ascii : 한글을 유니코드가 아닌 원본으로 출력
# indent : 보기 좋게 바꿔주며, 전달한 값은 들여쓰기 공백 개수이다.
json_data = json.dumps(data, ensure_ascii=False,indent=4)
print(json_data)

# json 을 dick로 변환

data_dict = json.loads(json_data)
print(data_dict)