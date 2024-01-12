# #인덱스 슬라이싱
# animals  = ['dog', 'dog', 'cat', 'bird', 'fish']
#
# # list[inclusive_strat=0 : exclusive_len(list)] - list
#
# print(animals [0])
# print(animals [0:3])
# print(animals[1:4])
# print(animals[:2])
# print(animals[2:])
#
# # list[inclusive_strat=0 : exclusive_len(list): step=1] - list
# foods = ['noodel', 'meat', 'bread','chicken']
# print(foods[:3:2])
# print(foods[2::2])
#
# # 역순출력
#
# print(foods[::-1])

# number_list = list(range(1,11))

# [1,3,5,7,9]
# print(number_list[::2])

# [6,5,4,3,2]
# print(number_list[-5:-10:-1])

# [2,4,6]
# print(number_list[1:6:2])

# [2,3,4,5,6,7]
# print(number_list[1:7])

# animals = ['dog', 'dog', 'cat','bird']
# zoo = ['panda', 'giraffe']
#
# animals[1:2] = zoo
# print(animals)
#
# animals.insert(animals.index('dog')+1,'giraffe')
# print(animals)
#
# animals.insert(animals.index('dog')+1, zoo)
# print(animals)

# 슬라이싱, insert, del 를 사용하여 아래의 list 만들기
# ['dog', 'hamster', 'fish', 'dog' 'whale', 'bird']

# animals = ['dog', 'dog', 'cat', 'bird']
#
# animals.insert(animals.index('dog')+1,'hamster')
# animals.insert(animals.index('hamster')+1,'fish')
# # animals[4] = 'whale'
# del(animals(animals.index('cat')))
# animals.insert(animals.index('bird'),'whale')
# print(animals)

















