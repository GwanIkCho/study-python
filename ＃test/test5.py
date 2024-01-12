#  for문을 이용하여 역 피라미드 만들기
#  exr
# *****
# ****
# ***
# **
# *

# jump = ""
#
# for i in range(6):
#     for j in range(0,6-i):
#         jump += "*"
#     jump += '\n'
#
# print(jump)

# if문 활용한 학점계산기
# m = '점수를 입력하세요(국어/영어/수학)'
# m1 = 'ex)100,45,50'
#
# a, b, c = map(int,input(m+'\n'+m1+'\n').split(','))
# result = (a+b+c) // 3
#
# if result >= 90:
#     total = 'A'
# elif result >= 80:
#     total = 'B'
# elif result >= 70:
#     total = 'C'
# elif result >= 60:
#     total = "D"
# else:
#     total = "ㅎㅎ"
#
# print(f'당신의 평균은{result}이며 학점은{total}입니다')

# while문으로 키오스크? 만들기

# money = 0
# while True:
#     num = int(input('무엇을 주문하시겠습니까\n1.아아 : 2000\n2.라떼 : 2500\n3.아이스티 : 1500\n4.주문종료\n'))
#     if num == 1:
#         print('아아 한잔 주문완료.')
#         money += 2000
#     elif num == 2:
#         print('라떼 한잔을 주문완료.')
#         money += 2500
#     elif num == 3:
#         print('아이스티 한잔 주문완료')
#         money += 1500
#     elif num ==4:
#         print('주문을 완료하였습니다 총 가격은 %d원 입니다.'%money)
#         break
#     else:
#         print('잘못입력하셨습니다.')

# 구구단 만들기

# m = '구구단을 만들 정수를 입력하세요'

# number = int(input(m+'\n'))
#
# for i in range(9):
#     print(f'{number}*{i+1} = {number*i+1}')

# 윤년 검사기
# 참조 4년단위로 윤년입니다^^
#
# m = '년도를 입력하세요'
# ex = 'ex) 2024'
#
# year = int(input(m+'\n'+ex+'\n'))
# if year % 4 == 0:
#     print('윤년입니다')
# else:
#     print('아니에요^^')



