# annimal = ['dog', 'cat', 'bird', 'fish']
# # print(annimal)
# # print(type(annimal))
#
# # 인덱스로 접근
# # print(annimal[1])
# # print(annimal[2])
#
# # 음수 인덱스 가능(가장 마지막부터 순서대로 앞으로 이동한다.)
# # print(annimal[-1])
# # print(annimal[-2])
#
# # len()
# # print(len(annimal))
#
# # append()
# annimal.append('hamster')
# print(len(annimal))
#
# annimal.append('cat')
# print(annimal)
#
# # insert()
#
# annimal.insert(1,'dog')
# print(annimal)
#
# # remove()
# annimal.remove('fish')
# print(annimal)
#
# # del()
# del(annimal[1])
# print(annimal)
#
# # clear()
# # annimal.clear()
# # print(annimal)
#
# # index()
# print(annimal.index('bird'))
# # print(annimal.index('tiger'))
#
# # 수정
# index = annimal.index('bird')
# annimal[index] = 'lion'
# print(annimal)

# 그 외
# animals = ['dog', 'cat', 'bird', 'fish']
# print(animals*2)
#
# print('dog' in animals)
# print('tiger' in animals)
#
# for animal in animals:
#     print(animal)

# 실습
# 1~90까지 list에 담고 출력

# list = list(range(1,90,1))
# print(list)

# number_list = [0]*90
# for i in range(len(number_list)):
#     number_list[i] = i+1

# print(number_list)


# 1~100까지 중 짝수만 list에 담고 출력

# list = list(range(2,100,2))
# print(list)

# number = [0]*50
#
# for i in range(len(number)):
#     number[i] = i*2
#
# print(number)


# 1~10까지 리스트에 담은 후 짝수만 출력

# list = list(range(1,11,1))
#
# for n in list:
#     if not n % 2:
#         print(n)
#
# print()

# number = []
#
# for i in range(10):
#     number.append(i+1)
# for i in range(len(number)):
#     if number[i]%2 == 0:
#         print(number[i])


# 4명의 회원 정보를 list에 담은 뒤 두 번째 회원의 이름을 변경하고 마지막 회원은 삭제

# member = ['cho', 'kim', 'lee', 'choi']
#
# member[1] = 'park'
#
# member.remove(member[-1])
# del member[-1]
# print(member)


# "189,000원"을 189000으로 변경

# lsit 안에 list
number_list = [[1,3,5], [2,4,6]]
# print(number_list[0][0])

for i in range(len(number_list)):
    for j in range(len(number_list[i])):
        print(number_list[i][j])
















