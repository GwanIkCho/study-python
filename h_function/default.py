# 만약 값을 매개변수로 전달하지 않았을 경우
# 기본값을 설정할 수 있고, arg = avlue로 작성한다.

def sub(number1, number2 ,number3, number4=0 ):
    return number1 - number2 - number3 - number4

result = sub(10,20,30,40)
print(result)

# 실습

# 이름을 전달받지 못하면 '익명'으로 대체하고,
# 나이를 전달받지 못하면 0으로 대체한다.

def get_info(name='익명',age=0):
    # return name,age
    return {'name': name,'age':age}


print(get_info(name='cho'))
print(get_info(age=20))
print(get_info(name='cho', age=20))