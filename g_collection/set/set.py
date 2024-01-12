# 중복이 없고, 순서가 없다(값을 가져올수 없다). - 중복 검사용
# world_set = {'korea', 'america','japan', 'china'}
# print(type(world_set))
# print(len(world_set))
#
# list = list(world_set)
# print(list)

# 가져오는건 다른구조로 변환후 가져오는거임 원래는 직접가져오기 불가
# world_set.add('korea')
# print(world_set)

# 중복을 제거할때 효과적이다.
# datas = [1,2,2,1,3,2,1,3,4,2,5,1,6]
# print(list(set(datas)))