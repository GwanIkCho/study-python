# # 파일의 단어의 빈도수 구하기
#
# # alice.txt
#
# # 오로지 알파벳만 검사하기
# # 대소문자 구문없이 비교
# # 글자수 2개 이상인 단어만 카운트 하기
# # 빈도수 100회 이상인 단어만 카운트
# # 전체 내용을 문자열로 가져오기: file.read()
#
# with open('alice.txt', 'r', encoding='utf-8') as file:
#     content = file.read().lower()
#     # content는 엘리스 파일을 전체 소문자로 만들어둠
#
#
# result = ''
#
# for i in content:
#     #  전체에서 글자만큼 돌려봅니다
#     if 'a' <= i <='z':
#         # 문자면 그 문자는 result에 담아요
#         result += i
#         continue
#     # 만약 문자가 아니면 그냥 띄어쓰기로 남깁니다. 안그러면 글자분리 못해요
#     result += ' '
#
# # 그러면 순수하게 소문자 알파벳만 남은 친구들이 남아요
# # 알파벳이랑 띄어쓰기만 한 친구들을 단어단어마다 남겨두고
# # 그 단어가 2글자 이상이면 word에 리스트로 담김니다.
# words = [word for word in result.split() if len(word)>1]
#
# wwords = {}
#
# # 단어 리스트로 담아둔것들을 이제 하나하나 나눠두고
# for word in words:
#     # 이제 딕셔너리로 저장하는데 그 단어가 딕셔너리에 저장되어있으면 이제 거기에 +1해주고
#     if wwords.get(word) is not None:
#         wwords[word] += 1
#     #없으면 새로 만들면서 1이라는 값을 설정해둠
#     else:
#         wwords[word] = 1
#
#
# #  담겨있는것들은    단어 :  값
# wwords = {word : wwords[word]
# #    전체중에서 담겼는것중에
# for word in wwords
#           #  값이 100이상인것만
#           if wwords[word] >=100}
#
# # wwords 중에서 단어들을 확인하는데 그 단어의 값이 100이상인것만 살려둔다.
#
# sorted_key = sorted(wwords, key=wwords.get, reverse=True)
# for key in sorted_key:
#     print(key, wwords[key])
#


with open('alice.txt','r', encoding='utf-8') as file:
    content = file.read().lower()


temp= ''

for i in content:
    if 'a'<= i <= 'z':
        temp += i

    else:
        temp = ' '



print(temp)
