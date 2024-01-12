# # # # 추가, 수정, 삭제, 검색, 목록
# # # # 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# # # # 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# # # # 가격 검색 시 오차 범위는 ±50%로 설정한다.
# # name_list = []
# # price_list = []
# #
# # title = "또와 과일"
# # menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
# # search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
# # append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
# # search_name_message_for_update = '수정하실 상품명을 입력하세요.'
# # update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
# # delete_message = '삭제하실 상품명을 입력하세요.'
# # search_name_message, search_price_message = '상품명: ', '가격: '
# #
# #
# # append_error_message = "추가 실패(중복된 상품명)"
# # update_error_message1 = "수정 실패(존재하지 않는 상품명)"
# # update_error_message2 = "수정 실패(중복된 상품명)"
# # delete_error_message = "삭제 실패(존재하지 않는 상품명)"
# # search_name_error_message = "검색 실패(존재하지 않는 상품명)"
# # search_error_message = "검색 결과가 없습니다."
# # error_message = "다시 입력해주세요."
# # no_item_message = "목록이 없습니다."
# # #
# #
# # #  name이 담기는곳
# # name_list = []
# # # price가 담기는곳
# # price_list = []
# # # 위에있는 erreo메세지들이 여기에 담겨서 프린트 됩니다.
# # result_message = ''
# #
# # #  list형 문제
# # while True:
# #     # 전체 메뉴를 사용사가 선택할수있게 input에 담아주고 choice가 받을수 있게 int형으로 바꿔준다
# #     choice = int(input(menu))
# #     # 추가 / 사용자가 1을 선택한다면
# #     if choice == 1:
# #         #     받아햐나는거 name / print 2개를 받아야한다.
# #         new_name, new_price = input(append_message).split()
# #         # 기존에 있는거인지 비교는 한번 해줘야합니다.
# #         if new_name not in name_list:
# #             # name_list에 새로운 이름을 담아줍니다.
# #             name_list.append(new_name)
# #             # price_ist에 담아줍니다. 근데 이건 정수로 담아야해서 int추가
# #             price_list.append(int(new_price))
# #         # if 반대로 이름 같은게 있으면
# #         else:
# #             result_message = append_error_message
# #
# #     # 수정 / 사용자가 2를 선택한다면
# #     elif choice == 2:
# #         # 먼저 어떤걸 수정할건지 물어봅니다.(name만)
# #         name = input(search_name_message_for_update)
# #         #  사용자에게 받은 name이 name_list에 있는지 확인하고
# #         if name in name_list:
# #             # 새로운 이름,가격을 받는다.
# #             new_name, new_price = input(update_message).split()
# #             # 새로 받은것도 중복된게 없다면
# #             if new_name not in name_list:
# #                 #     name에 인덱스 번호를 확인한다
# #                 index = name_list.index(name)
# #                 name_list[index] = new_name
# #                 price_list[index] = int(new_price)
# #             else:
# #                 result_message = update_error_message2
# #         else:
# #             result_message = update_error_message1
# #
# #     # 삭제 / 사용자가 3을 선택하면
# #     elif choice == 3:
# #         # 삭제하려는 과일을 물어봅니다.
# #         name = input(delete_message)
# #         # 만약 리스트에 그 이름이 있다면
# #         if name in name_list:
# #             # 그 이름에 맞는 인덱스 값을 찾아준 뒤
# #             index = name_list.index(name)
# #             del name_list[index]
# #             del price_list[index]
# #         else:
# #             result_message =delete_error_message
# #     # 검색 / 사용자가 4를 선택하면
# #     elif choice == 4:
# #         # 검색하고자 하는 이름인지 가격인지물어본다. / 이름, 가격 따로 검색을 만들어준다.
# #         choice = int(input(search_menu))
# #         #  1 이름으로 검색
# #         if choice == 1:
# #         #     이름이 뭔지 물어본다.
# #             new_name = input(search_name_message)
# #             # 만약 리스트에 작성한 이름이 있다면
# #             if new_name in name_list:
# #                 # 이름의 인덱스를 확인하고
# #                 index = name_list.index(new_name)
# #                 print(f'상품명 : {name_list[index]}, 가격{price_list[index]}')
# #             else:
# #                 result_message =search_name_error_message
# #
# #         #  2. 가격으로 검색
# #         elif choice == 2:
# #             # 검색할 가격을 받고
# #             new_price = int(input(search_price_message))
# #             # 그 가격이 리스트에 있다면
# #             if new_price in price_list:
# #                 # 가격 인덱스 확인하고
# #                 index = price_list.index(new_price)
# #                 print(f'상품명 : {name_list[index]}, 가격 : {price_list[index]}')
# #             else:
# #                 result_message =search_name_error_message
# #
# #         else:
# #             result_message = search_name_error_message
# #
# #     # 목록 / 사용자가 5를 선택하면
# #     elif choice == 5:
# #         # 목록에 결과 값이 있다면 보여주고 없다면 메시지 전송하기
# #         if len(name_list) ==0:
# #             result_message = no_item_message
# #
# #         else:
# #             for i in range(len(name_list)):
# #                 print(f'{name_list[i]},{price_list[i]}',end='\n')
# #
# #     # 나가기(끝내기) /사용자가 6을선택한다면
# #     elif choice == 6:
# #         # while 반복문을 끝내기 위해 break를 사용한다.
# #         break
# #
# #     else:
# #         result_message = error_message
# #         print(result_message)
# #         result_message= ''
# #
# #
# # print(menu)
# # 추가, 수정, 삭제, 검색, 목록
# # 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# # 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# # 가격 검색 시 오차 범위는 ±50%로 설정한다.
#
#
# title = "또와 과일"
# menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
# search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
# append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
# search_name_message_for_update = '수정하실 상품명을 입력하세요.'
# update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
# delete_message = '삭제하실 상품명을 입력하세요.'
# search_name_message, search_price_message = '상품명: ', '가격: '
#
# result_message = ""
# append_error_message = "추가 실패(중복된 상품명)"
# update_error_message1 = "수정 실패(존재하지 않는 상품명)"
# update_error_message2 = "수정 실패(중복된 상품명)"
# delete_error_message = "삭제 실패(존재하지 않는 상품명)"
# search_name_error_message = "검색 실패(존재하지 않는 상품명)"
# search_error_message = "검색 결과가 없습니다."
# error_message = "다시 입력해주세요."
# no_item_message = "목록이 없습니다."
#
#
# # 리스트 ㄴㄴ dict임  여기는 key : value 이런식으로 담김 data_list[key] = value 로 담을수 있음 그럼 왼쪽처럼 담김
# start = title + '\n' + menu
# data_dict = {}
#
#
# while True:
#     # 사용자에게 메뉴를 보여주고 선택한 번호를 choice에 저장
#     choice = int(input(title + '\n' + menu))
#     # 추가 / 사용자가 1을 선택한다면
#     if choice == 1:
#         # 추가하고 싶은 상품,가격을 물어본다
#         new_name,new_price = input(append_message).split()
#         # 새로운 이름이 딕셔너리에 없다면
#         if new_name not in data_dict:
#             # 딕셔너리에 / 새로운이름 : 가격/ 을 추가해준다
#             data_dict[new_name] = int(new_price)
#         else:
#             # 같은이름이 있으니 경고 메시지를 보내준다.
#             result_message = append_error_message
#
#     # 수정 / 사용자가 2를 선택한다면
#     elif choice == 2:
#         # 수정할 이름을 받는다
#         name = input(search_name_message_for_update)
#         # 만약 dict에 겹치는 이름이 있다면
#         if name in data_dict:
#             # 새로운 상품, 가격을 받는다
#             new_name, new_price = input(update_message).split()
#             # 새로받은 이름이 dict에 있으면
#             if new_name in data_dict:
#                 # 기존이름은 지워주고
#                 del data_dict[new_name]
#                 #  새로운 친구들을 추가해준다
#                 data_dict[new_name] = int(new_price)
#             else:
#                 # 같은이름이 있다고 알려준다.
#                 result_message =update_error_message2
#         else:
#             # 현재 dict에 없다고 알려준다
#             result_message =update_error_message1
#     # 삭제하기
#     elif choice == 3:
#         # 삭제하고싶은 키값을 물어본다
#         name = input(delete_message)
#         # dict에 검색한 이름이 있다면
#         if name in data_dict:
#             # 그 이름을 dict에서 지워준다 (키값 지우면 value 값도 사라짐)
#             del data_dict[name]
#         else:
#             # dict에 없는 메시지라고 알려준다.
#             result_message = delete_error_message
#
#     # 검색하기 / 검색은 이름, 가격 나눠서 해야함, / 사용자가 4를 선택했을때
#     elif choice == 4:
#         # 검색을 이름할지 가격할지 물어봐야함
#         choice = int(input(search_menu))
#         # 이름을 검색한다면
#         if choice == 1:
#             # 이름이 뭔지 물어봄,
#             name = input(search_name_message)
#             # dict에 있다면
#             if name in data_dict:
#                 for key, value in data_dict.items():
#                     print(f'상품명 : {key}, 가격,{value}')
#             else:
#                 result_message = search_name_error_message
#         # 가격으로 검색한다면
#         elif choice == 2:
#             # 가격이 얼마인지물어봐야함
#             # 가격을 받습니다.
#             price_input = int(input('얼마인가요'))
#             # 있는지 확인하기 위해 value를 추출
#             for key, value in data_dict.items():
#                 if price_input == value:
#                     print(f'{key},{value}')
#             else:
#                 result_message =search_name_error_message
#
#     # 목록보기 / 사용자가 5를 선택했을때
#     elif choice == 5:
#         # 목록이 있을때와 없을때를 나눠서 설명해야함
#         if len(data_dict) == 0:
#             # 목록이 없을때없다고 알려줌
#             result_message = no_item_message
#
#         elif len(data_dict) != 0:
#             for key, value in data_dict.items():
#                 print(f'{key},{value}')
#
#
#         pass
#     # 나가기 / 이용 종료를 원하면 / 사용자가 6을 선택했을때
#     elif choice == 6:
#         # while 반복문을 멈춰준다.
#         break
#     # 그 외(에러)
#     else:
#         result_message = error_message

# print(start)

# function.py 문제
# # 1~n까지의 합을 구해주는 함수

# def add(n):
#     # 1~n까지 반복하는 함수를 만들어준다
#     total = 0
#     for i in range(n):
#         total += i+1
#     return total
#
# print(add(4))


# # 1~100까지 중 n의 배수를 print()로 출력하는 함수

# def add(n):
#     '''
#     :param n: n 의 배수
#     :return:
#     '''
#     # 1~100을 만들어줘야함
#     for i in range(100):
#         # i+1 = 1~100 이고 / n 의 으로 나눴을때 나머지가 없으면 n의 배수
#         if (i+1) % n == 0:
#             print(f'100이하 n의 배수는 {i+1}')
#
#
# print(add(5))

# # 문자열을 입력받고 원하는 문자의 개수를 구해주는 함수

# def word(key,check):
#     '''
#     :param key: 문자열
#     :param check: 체크할 글자
#     :return:
#     '''
#     # key글자수 i만큼 반복(key글자수)
#     count = 0
#     for i in key:
#         if i == check:
#             count += 1
#     return count
# print(word('AsaA','A'))

# 문자열에서 'A'가 몇개있는 지 검사하는 함수

# def check(st):
#     '''
#     :param st: 문자열
#     :return:  'A' 만날때마다 count늘리기 위해 count로
#     '''
#     # A만날때마다 카운트늘려줘야해서 추가
#     count = 0
#     # st글자수 만큼 i(st글자수)번 반복함
#     for i in st:
#         if i == 'A':
#             count += 1
#     return count
# 여러개의문자열에서 'A'가 몇개있는 지 검사하는 함수

# def check(*st):
#     '''
#     :param st: 문자열들
#     :return: count 받아줘여해서 count
#     '''
#
#     result = []
#     count = 0
#     # 문자열 갯수만큼 i 번 읽음
#     for i in st:
#         for j in i:
#             if j == 'A':
#                 count += 1
#         result.append(count)
#         count = 0
#
#     return result


# print(check('ASD','AAAA','SDS'))

# 다 하고 packig 한번 읽고

#  kwargs.py
# 주문 가격과 주문한 회원의 정보 출력
# def check(*price,**kwargs):
#     '''
#     :param price: 다수의 주문횟수들
#     :param kwargs: name : 'name'
#     :return: 주문할때마다 가격을 올려줘야하니 count
#     '''
#
#     count = 0
#     for i in range(len(price)):
#         count += price[i]
#     print(f'총 주문금액은{count}이며 주문자는{kwargs["name"]}')
#
#     return count
#
# print(check(100,100,400, name= 'cho',))


# 국어, 영어, 수학 점수의 평균 구하기

# def total(**kwargs):
#     '''
#     :param kwargs: kor : 00 eng : 00 math:00
#     :return: 점수 총합 구하는곳 count로
#     '''
#
#     count = 0
#     kor = kwargs['kor']
#     eng = kwargs['eng']
#     math = kwargs['math']
#     totlaa = (kor+eng+math) // len(kwargs)
#     print(f'국어는{kwargs["kor"]},영어는{kwargs["eng"]},수학은{kwargs["math"]}이며 총 평균운 {totlaa}입니다')
#
# print(total(kor=100, eng=75,math =50))

# 다음 basic - intermediate 풀기

# 회원의 주문 금액(pay)와 회원의 할인율과 개수(coupion, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# (선택사항) comprehension을 사용한다.



# def test(*args, **kwargs):
# #     '''
# #     :param args: 총 숫자는 주문횟수, 각 숫자별로는 주문가격
# #     :param kwargs: coupion : 할인율   / count : 쿠폰 개수
# #     :return:
# #     '''
# #     result_list = []
# #     # 쿠폰숫자랑 할인율도 적용해야 하니때문에 꺼낸다
# #     coupion, count = kwargs['coupion'], kwargs['count']
# #     # args가 주문횟수 + 각 주문별로 할인받을지도 해야해서 각자 계산들어가야함 각자 계산결과를 보여야 해서 list로 담
# #     for i in range(len(args)):
# #         # 인덱스 번호 비교했을때 쿠폰이 부족하고 i가 더 커졌을때
# #         if i >= count:
# #             # args[i]를 통해 args인덱스값 0,1,2를 순차적으로 resilt_list에 담는다.
# #             result_list.append(args[i])
# #         # 반대로 쿠폰이 더 많거나 같을경우에 할인율을 적용한다.
# #         else:
# #             # args에 할인율 적용해서 사용자가 지불할 값을 보여주고 list에 담는다.
# #             result_list.append(args[i]*(100-coupion)//100)
# #     # 모든 결과는 result_list에 담겨있어 그 값을 출력해준다.
# #
# #     return result_list
# #     print(result_list)
# #
#
#     coupion, count = kwargs['coupion'], kwargs['count']
#     # return [args[i]*(100-coupion) // 100 if i < count else args[i] for i in range(len(args))]
#
#     return [args[i]*(100-coupion)//100 if i < count else args[i] for i in range(len(args))]
#
#
# print(test(1000,2000,3000,coupion=10,count=2))



user_info = [
    {'number': 1, 'name': 'john'},
    {'number': 2, 'name': 'mike'},
    {'number': 3, 'name': 'ted'},
    {'number': 4, 'name': 'lindy'},
    {'number': 5, 'name': 'adam'},]
# # 추가

# number = 5
# def insert(name):
#     '''
#     :param kwargs: number : number / 'name' :name
#     :return:
#     '''
#     global number
#     number += 1
#     user_info.append({'number': number, 'name': {insert()}})
#
# print(insert(name='cho'))


# # 목록
# 조회(번호로 조회)
# # 수정(번호로 이름 수정)
# # 삭제(번호로 삭제)

