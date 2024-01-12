#  문자열끼리만 연결(+)이 가능하다.
# print('안'+ str(3))
import sys

# name = input("이름 : ")

# formating = f'{name}님 환영합니다.';
# print(formating)

#  제 이름은 ???, 키는 ??? cm입니다

# name = input("이름 : ")
# height = input("키 : ")

# formating = f'제 이름은{name}이고 키는 {height}cm 입니다.'
# print(formating)


#  두 정수를 입력받은 후곱셈 결과 출력
#  input('') 사용자가 입력한 문자열 값



# number1 = int(input('정수1 : '))
# number2 = int(input('정수2 : '))
#
# number3 = number1 * number2
#
# formatting = f'두 정수의 곱은 {number3}입니다.'
# print(formatting)

# message1 = '첫번째 정수 : '
# message2 = '두번째 정수 : '
#
# number1 = int(input(message1))
# number2 = int(input(message2))
# result = number1 * number2
#
# formatting = f'두 정수의 곱은{total}입니다.'
# print(formatting)


# map(각각 어떻게 바꿀 것인가, [])
# message = '두정수를 입력하세요.'
# exaple_message = '예) 1, 3'
# number1, number2 =  map[int, input(message +'\n'+ exaple_message+'\n'.split(', '))]
# result = number1 * number2
# formmating = f'{number1}, {number2} = {result}'




# #  현재 시간을 입력하고 시와 분으로 분리하여 출력

# 현재 시간을 입력하고 시와 분으로 분리하여 출력
# message = '현재 시간: '
# time = input(message)
# hours, minutes = time.split(':')
# formatting = f'{hours}시 {minutes}분'
#
# print(formatting)

#  핸드폰 번호를 -(하이폰)과 함께 입력받은 뒤 각 자리의 번호를 분리해서 출력

# numbers = input('전화번호를 입력해주세요\nex) 000-0000-0000\n')
#
# number1, number2, number3 = numbers.split('-')
#
# formmating = f'1: {number1}2: {number2}3: {number3}'
# print(formmating)

#  이름과 나이를 한번에 입력받은 뒤 "000님의 나이는 00살" 형식으로 출력
#
# name = input('이름 : ')
# age = int(input('나이 : '))

# message = '이름과 나이를 입력하세요'
# ex = '홍길동 20'
#
# name, age = input(message+'\n'+ex+'\n').split()
#
# formmating = f'{name}님의 나이는 {age}살'
# print(formmating)


# formmating = f'{name}의 나이는 {age}살'
# print(formmating)


#  3개의 정수를 입력받은 뒤 덧셈결과 출력

# number1 = int(input('정수1 : '))
# number2 = int(input('정수2 : '))
# number3 = int(input('정수3 : '))
#
# total = number1 + number2 + number3
#
# formmating = f'세 정수의 합은 {total}입니다.'

# print(formmating)


message = '3개의 정수를 입력하세요'
ex = '1/2/3'

number1, number2, number3 = map(int, input(message+'\n'+ex+'\n').split('/'))
result = number1+number2+number3
formmating = f'3정수의 합은{result}입니다'

print(formmating)
