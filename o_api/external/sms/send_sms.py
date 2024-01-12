# import json
# import message
#
# # 한번 요청으로 1만건의 메시지 발송이 가능합니다.
# if __name__ == '__main__':
#     data = {
#         'messages': [
#             {
#                 'to': '01039690009',
#                 'from': '01039690009',
#                 'text': '테스트 문자'
#             }
#
#         ]
#     }
#     res = message.send_many(data)
#     print(json.dumps(res.json(), indent=2, ensure_ascii=False))
