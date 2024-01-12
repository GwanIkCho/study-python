# email을 입력받고 아이디와 도메인을 각각 분ㄹ하여 출력한다.

# message = '이메일을 입력해주세요'
# exaple_message = 'asd123@gmail.com'
#
# main, sub = input(message+'\n'+exaple_message+'\n').split('@')
# formmating = f'아이디는 {main}\n도메인은 {sub}입니다'
# print(formmating)


#     첫 번째 값으로 야드를 입력받고, 두 번째 값으로 인치를 입력받아서
#     각각 cm로 변환하여 다음 형식에 맞추어 소수점 둘 째자리까지 출력한다.
#
#     1yd: 91.44cm
#     1in: 2.54cm
#
#     예)
#         yard 입력: 10
#         inch 입력: 10
#
#         10 yard는 914.4cm
#         10 inch는 25.4cm
#  round(값, 원하는 자리수) : 소수점이 맞춰진 결과값

# message1 = '변환할 야드를 입력하세요'
# message2 = '변환할 인치를 입력하세요'
#
# exaple_message = '10,10'
#
# yard, inch = map(int,input(message1+'\n'+message2+'\n'+exaple_message+'\n').split(','))
#
# formmating = f'yard 입력 : {yard}\ninch 입력 : {inch}\n\n 10yard는 {yard*91.4}cm\n10inch는 {inch*25.4}cm'
# print(formmating)

yard_message = 'yard 입력 : '
inch_message = 'inch 입력 : '

yard = float(input(yard_message))
inch = float(input(inch_message))

yard_to_cm = round(yard * 91.44, 2)
inch_to_cm = round(inch * 2.54, 2)

yard_formatting = f'{yard}yard는 {yard_to_cm}cm'
inch_formatting = f'{inch}inch는 {inch_to_cm}cm'

print(yard_formatting, inch_formatting,sep='\n')



