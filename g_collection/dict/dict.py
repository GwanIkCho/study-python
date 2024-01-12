# student = {
#     'name': 'cho',
#     'email': 'iki980411@naver.com'
# }
#
# # print(student['name'])
# # print(student.get('name'))
#
# # get을 사용하면 key를 찾지 못했을 때 원하는 default 값으로 설정이 가능하며,
# # default값이 없을때에는 None을 가져온다
# # print(student['phone'])
# # print(student.get('phone', '123132'))
#
# # 'name' key값이 이미 있기 때문에, 아래 코드는 수정이다.
# student['name'] = 'kim'
# print(student)
#
# # 'phone' key값이 없기 때문에, 아래의 코드는 추가이다.
# student['phone'] = '010123456'
# print(student)
#
# # 이미 있으니 수정
# if 'email' in student:
#     student['email'] = 'hong@naver.com'
# #  없으니 추가
# else:
#     student['email'] = 'hong@naver.com'
#
# print(student)

# my_dict = {
#     1: 'cho',
#     'two': '20살',
#     False: [10,20,30],
#     'row': [
#         {'name':'ted', 'age':40},
#         {'name':'jack', 'age':30},
#         {'name':'john', 'age':20}
#     ]
# }

#  row에 있는 회원 3명의 정보를 모두 출력

# if 'row' in my_dict:
#     for data in my_dict['row']:
#         print(f'{data["name"]}: {data["age"]}')

# 1~10중 홀수와 짝수가있다.
# 사용자가 짝수를 입력하면, 짝수만 출력하고
# 홀수를 입력하면 홀수만 출력한다.
# dict 사용

# num_dict = {'짝':[i *2 +1 for i in range(5)],
#             '홀':[(i+1)*2 for i in range(5)]}
#
# print(','.join(map(str,num_dict[input('홀짝')])))

# m = '숫자'
# a = int(input(m))
#
# if a % 2 ==0:
#     print(num_dict['num'])
# else:
#     print(num_dict['num2'])

student = {
    'name': 'cho',
    'email': 'iki980411@naver.com'
}

# # # key 분리
# # print(list(student.keys()))
# #
# # # value분리
# # print(list(student.values()))
# # # item분리
# print(list(student.items()))
#
# # for value in student.items():
# #     print(value)