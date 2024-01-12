# # 추가, 수정, 삭제, 검색, 목록
# # 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# # 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# # 가격 검색 시 오차 범위는 ±50%로 설정한다.
# name_list = []
# price_list = []
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
# while True:
#     choice = int(input(title+'\n'+menu))
#     if choice == 1:
#         name, price = input(append_message).split()
#         if name not in name_list:
#             name_list.append(name)
#             price_list.append(int(price))
#             continue
#         else:
#             result_message = append_error_message
#
#     elif choice == 2:
#         name = input(search_name_message_for_update)
#         if name in name_list:
#             new_name, new_price = input(update_message).split()
#             if new_name not in name_list:
#                 index = name_list.index(name)
#                 del name_list[index],price_list[index]
#                 name_list.append(new_name)
#                 price_list.append(int(new_price))
#             else:
#                 result_message = update_error_message2
#         else:
#             result_message =update_error_message1
#
#     elif choice == 3:
#         name = input(delete_message)
#         if name in name_list:
#             index = name_list.index(name)
#             del name_list[index],price_list[index]
#         else:
#             result_message = delete_error_message
#     elif choice == 4:
#         choice = int(input(search_menu))
#         if choice == 1:
#             name = input(search_name_message)
#             if name in name_list:
#                 index = name_list.index(name)
#                 print(f'이름 : {name_list[index]}, 가격 {price_list[index]}')
#             else:
#                 result_message = search_name_error_message
#         elif choice ==2:
#             price = int(input(search_price_message))
#             max = price * 1.5
#             min = price * 0.5
#
#             if min <= price <= max:
#                 # 이러면 그냥 price 찾는거임
#                 index = price_list.index(price)
#                 print(f'이름 : {name_list[index]}, 가격 {price_list[index]}')
#             else:
#                 result_message = search_name_error_message
#         pass
#     elif choice == 5:
#         if len(name_list) == 0:
#             result_message = no_item_message
#         else:
#             # 이러면 따로 보여줘야하는데 반복문으로 돌리면 하나씩 따로 볼수있음
#             print(f'{name_list}\n{price_list}')
#     elif choice == 6:
#         print('감사합니다')
#         break
#
#     else:
#         print(result_message)
#
# print(result_message)
#




# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
# data_dict = {}
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
# while True:
#     choice = int(input(title+'\n'+menu))
#     if choice == 1:
#         name, price = input(append_message).split()
#         if name not in data_dict:
#             data_dict[name] = price
#         else:
#             result_message = append_error_message
#
#     elif choice == 2:
#         name = input(search_name_message_for_update)
#         if name not in data_dict:
#             new_name, new_price = input(update_message)
#             if new_name not in data_dict:
#                 data_dict[new_name] = new_price
#             else:
#                 result_message = update_error_message2
#         else:
#             result_message = update_error_message1
#     elif choice == 3:
#         name = input(delete_message)
#         if name in data_dict:
#             del data_dict[name]
#         else:
#             result_message = delete_error_message
#     elif choice == 4:
#         choice = int(input(search_menu))
#         if choice == 1:
#             name = input(search_name_message)
#             if name in data_dict:
#                 print(f'{name} {data_dict[name]}')
#             else:
#                 result_message = search_error_message
#         elif choice == 2:
#             check_price = int(input(search_price_message))
#             max = check_price * 1.5
#             min = check_price * 0.5
#
#             for name, price in data_dict.items():
#                 if min <= price <= max:
#                     print(f'{name} {data_dict[name]}')
#                 else:
#                     result_message = search_error_message
#
#     elif choice == 5:
#         if len(data_dict) == 0:
#             result_message = no_item_message
#         else:
#             for name,price in data_dict.items():
#                 print(f'{name} {price}')
#
#
#
#     elif choice == 6:
#         break
#
# print()






# # 문자열에서 'A'가 몇개있는 지 검사하는 함수

# def stt(*args):
#     result = []
#     count = 0
#     for i in range(len(args)):
#
#         for j in args[i]:
#
#             if j == 'A':
#                 count +=1
#         result.append(count)
#         count = 0
#     return result
#
# print(stt('AAA','ABC','aaa'))


# # packing으로 제작하기
# # 국어, 영어, 수학 점수의 평균 구하기

# def ave(**kwargs):
#     kor, math, eng = kwargs['국어'], kwargs['수학'], kwargs.get('영어')
#     result = (kor + math + eng) / len(kwargs)
#     print(result)
#
# ave(국어=100,수학=80,영어=60)




# # 사용자가 원하는 자리수에서 반올림해준다.
# # 자리수를 받지 않았다면 기본값을 리턴한다.
#
# # 회원의 주문 금액(pay)와 회원의 할인율과 개수(coupion, count)를 전달받은 뒤
# # 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# # 할인율이 적용된 주문 금액이 정수로 리턴된다.
# # 쿠폰의 할인율은 백분율로 되어있다.
# # 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# # (선택사항) comprehension을 사용한다.



# def discount(*args,**kwargs):
#     coupion, count = kwargs['coupion'], kwargs['count']
#     result_list = []
#     for i in range(len(args)):
#         if i > count:
#             result_list.append(args[i] * (100-coupion) // 100)
#
#     return result_list





# def func_basic(*args, **kwargs):
#     # 할인율, 개수 kwargs에서 가져오기
#     coupon, count = kwargs['coupon'], kwargs['count']
#     # 결과값?담는곳
#     result_list = []
#     # 반복횟수
#     for i in range(len(args)):
#         # 쿠폰 남은수 비교
#         if i >= count:
#             # args에 인덱스 값을 result값에다가 넣는다.
#             result_list.append(args[i])
#         #위에 쿠폰은 할인받는 인덱스값 요밑은 나머지 값
#         else:
#             # 인덱스 값 받는 순서에다가 할인율 적용해서 그 값을 저장공간에 담는다.
#             result_list.append(args[i]*(100-coupon) //100)
#     # 인덱스있는만큼 반복 / 쿠폰숫자에비교 있으면 if쪽 없으면 else쪽으로 결과값 반복
#     return result_list
#
#
# print(func_basic(100,200,300,coupon=50,count=5))







# # # user_info = [
# # #     {'number': 1, 'name': 'john'},
# # #     {'number': 2, 'name': 'mike'},
# # #     {'number': 3, 'name': 'ted'},
# # #     {'number': 4, 'name': 'lindy'},
# # #     {'number': 5, 'name': 'adam'},
# # # ]
#
# # # # 추가
#
# # # # 목록
#
# # # # 조회(번호로 조회)
#
#
# # # # 수정(번호로 이름 수정)
#
#
#
#
#
# #
# post_info = [
#     {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
#     {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
#     {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
#     {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
#     {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
# ]
#
# # 추가(조회수는 전달받지 않고 기본값 0으로 설정)
#
#
# # 목록(최신순으로 조회)
#
#
# # 조회(번호로 조회, 조회수 1 증가)
#
#
#
#
#
#
# # 수정(번호로 정보 수정)
#
#
#
# # 삭제(번호로 삭제)
#
#
#
# # 평균을 구해주는 데코레이터를 제작한다.
# # 여러 개의 정수를 전달받으면, 총 합을 직접 구해준 뒤 평균을 출력한다.
# # 총 합(total)과 개수(count)를 전달받으면, 총 합/개수로 평균을 출력한다.
# # 총 합을 구하는 함수를 제작한 뒤 데코레이터를 통해 평균도 같이 확인할 수 있어야 한다.


# a는 평균구하기 b는 총합구하기
def project(pro):
    def a(*args,**kwargs):
        total = 0
        if len(args) != 0:
            for i in range(len(args)):
                total += int(args[i])
                result = total / len(args)
        else:
            total, count = kwargs['total'], kwargs['count']
            result = total / count

        print(f'{result}')
        return a(*args,**kwargs)
    return(a)



@project
def b(*args,**kwargs):
    if len(args) != 0:
        for i in range(len(args)):
            total = int(args[i])
    else:
        total, count = kwargs['total'], kwargs['count']

    print(f'{total}')


b(1,2,3)
b(total=6,count=3)