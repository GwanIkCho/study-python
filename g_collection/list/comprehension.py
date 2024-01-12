# comprehension(어떤뜻을 내포하고있다.)

# 반복하거나 특정조건을 만족하는 list를 보다 쉽게 만들어 내기 위한 방법

# list comprehension
# [표현식 for 항목 in iterator (if 조건)]

# number_list = [1, 2, 3, 4]
# result_list = [num * 3 for num in number_list ]
# print(result_list)


# number_list = [1, 2, 3, 4]
#
# result_list = [number * 3 for number in number_list if number % 2 ==0]
# print(result_list)

# [표현식 if 조건 else 표현식 for 항목 in iterator]
# [1,6,3,12]

# number_list = [1,2,3,4]
# result_list = [number *3 if number % 2==0 else number for number in number_list]
# print(result_list)

#  아래의 리스트에서 양수만 추출한 뒤 새로운 list에 담기

# number_list = [10, 20, 30, -20, -3, 50, -70]
# # result_list = [number if number<0 else None for number in number_list]
# result_list = [number for number in number_list if number>0]
# print(result_list)

# n개의 0으로만채워진 list

# m = '입력할 0의 개수를 입력해주세요'
# n = int(input(m))
#
# list = [0] * n
# result_list = [0 for i in range(n)]
# print(result_list)

# 제곱의 결과가 10보다 큰 결과만 담은 list
# number_list = [1,-2,3,-4,5]
# result_list = [number for number in number_list if number ** 2 >10]
# print(result_list)

# 0~9까지 중 3의 배수만 담은 list

# [표현식 if 조건 else 표현식 for 항목 in iterator]

number_list = list(range(10))
# result_list = [number for number in number_list if number % 3 ==0 and number>0]
result_list = [args[i] for i in range(len(args))]
print(result_list)

# coupon, count = kwargs['coupon'], kwargs['count']


# result_list = [i for i in range(10) if  i % 3 == 0 and i>0]
# print(result_list)

# [~~ else for i in it if ~~~]
# def func_basic(*args, **kwargs):
#     coupon, count = kwargs['coupon'], kwargs['count']
#     result_list = []
#     return (i>=count if  args[i] for i in range(len(args)))
