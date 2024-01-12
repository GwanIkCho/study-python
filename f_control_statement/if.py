# number = 15
#
# if number % 3 == 0:
#     print(f'{number}는 3의 배수입니다.')
# if number % 5 == 0:
#     print(f'{number}는 5의 배수입니다.')


# number가 양수인지 음수인지 0인지 검사해보세요^^

# number = 3
#
# if number > 0:
#     print(f'{number} 는 양수입니다')
# elif number < 0:
#     print(f'{number} 는 음수입니다')
# elif number == 0:
#     print(f'{number}는 0입니다.')

# number = 1
#
# positive_condition = number > 0
# negative_condition = number < 0
# zero_condition = number == 0
#
# if positive_condition:
#     print(f'{number}는 양수입니다.')
# elif negative_condition:
#     print(f'{number}는 음수입니다.')
# else:
#     print(f'{number}는 0입니다.')

# 나이를 입력받은 후 미성년자인지 확인해보세용

# age = "나이를 입력해주세요"
#
# information = int(input(age)
# condition = 0 < information <= 19
# error_condition = information <= 0
#
# if condition:
#     print('당신은 미성년자 입니다')
# elif error_condition:
#     print('잘못입력하셨습니다.')
# else:
#     print('당신은 성인입니다.')
#

# 두 정수를 입력받은 후 대소비교 진행

# massage = '2개의 정수를 입력해주세요'
# ex = 'ex\n1,3'
#
# number1, number2 = map(int,input(massage+'\n'+ex+'\n').split(','))
#
# # 선언할때 넣을 값을 모를경우 초기값을 넣어준다.
# # 정수 : 0 실수 0.0 문자열 '' or "" 불린 false
#
# result_massage = ''
#
# 일괄처리란,
# 각 분기별로 결과를 처리하지 않고
# 모든 분기 종류 후 한번에 처리하는 것을 의미한다.

# if number1 > number2:
#     result_massage = f'{number1}가 더 큽니다'
# elif number1 < number2:
#     result_massage = f'{number2}가 더 큽니다'
# else:
#     result_massage = '숫자가 같습니다.'
#
# print(result_massage)


