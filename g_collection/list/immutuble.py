# import copy

# 얕은복사 - 기존의 값을 복사해서 새롭게 만들어내는 것을 의미한다.
# 새로운 주소에 할당하기 때문에 불변성이 보장된다.
# 얕은 복사 사용시, 두번째 접근부터는 불변성이 보장되지 않는다.

# datas = [1,2,3]
# datas_copy = copy.copy(datas)
# datas_copy[0] = 10
# print(datas_copy)


# datas = [1,2,3]
# datas_copy = datas[:]
# datas_copy[0] = 10
# print(datas_copy)
# print(datas)

# datas = [1, [1,2,3,4], [5,6,7,8]]
# datas_copy = copy.copy(datas)
# datas_copy[1][0] = 10
# print(datas_copy)
# 깊은복사
# 깊은복사 사용 시, 깊은 접근까지 모두 불변성이 보장된다.
# 너무 깊은 구조에서 사용할 때에는, 메모리 소모량이 증가하기 때문에.
# 불변성이 보장될 필요가 없을 때에는 사용하지 않는 것이 좋다.

# datas = [1, [1,2,3,4], [5,6,7,8]]
# datas_copy = copy.deepcopy(datas)
# datas_copy[1][0] = 10
# print(datas_copy)























