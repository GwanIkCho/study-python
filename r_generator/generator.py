# data_list = [i ** 2 for i in range(100)]
#
# print(data_list)


import os

data_generator = (i ** 2 for i in range(100))
print(next(data_generator))


