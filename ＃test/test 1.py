# 회원의 주문 금액(pay)와 회원의 할인율과 개수(coupion, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# (선택사항) comprehension을 사용한다.

def func_basic(*args, **kwargs):
    '''

    :param args: 주문 금액(pay)
    :param kwargs: 할인율과 개수
    :return: result_list -> 주문금액 + 쿠폰있으면 있는만큼 할인받고 뒤에 주문금액 추가
    '''

    coupion, count = kwargs['coupon'], kwargs['count']
    result_list=[]
    for i in range(len(args)):
        if i >= count:
            result_list.append(args[i])
        else:
            result_list.append(args[i] * (100 - coupion) // 100)

    return result_list


print(func_basic(3000,2000,1000,coupon=40,count=1))

#%%
# 회원의 주문 금액(pay)와 회원의 할인율과 개수(coupion, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# (선택사항) comprehension을 사용한다.



def func_basic(*args, **kwargs):
    # 할인율, 개수 kwargs에서 가져오기
    coupon, count = kwargs['coupon'], kwargs['count']
    # 결과값?담는곳
    result_list = []
    # 반복횟수
    for i in range(len(args)):
        # 쿠폰 남은수 비교
        if i >= count:
            # args에 인덱스 값을 result값에다가 넣는다.
            result_list.append(args[i])
        #위에 쿠폰은 할인받는 인덱스값 요밑은 나머지 값
        else:
            # 인덱스 값 받는 순서에다가 할인율 적용해서 그 값을 저장공간에 담는다.
            result_list.append(args[i] *(100-coupon) //100)
    # 인덱스있는만큼 반복 / 쿠폰숫자에비교 있으면 if쪽 없으면 else쪽으로 결과값 반복
    return result_list

    # result_list = [args[i] for i in range(len(args)) if ]

# (갸격,가격,가격,  key = value,key = value)
print(func_basic(5000,4000,1000,coupon=10,count=100))




# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# comprehension을 사용한다.

# 입력 예시1
# [2000, 4000, 5000]
# coupon=50
# count=2

# 출력 예시1
# [1000, 2000]

# 입력 예시2
# [1000, 4000, 5000]
# coupon=30
# count=100

# 출력 예시2
# [700, 2800, 3500]

def use_coupon(*pay, **kwargs):
    '''

    :param pay: 주문 금액들
    :param kwargs: {coupon: 할인율, count: 쿠폰의 개수}
    :return: 할인율이 적용된 주문 금액들
    '''
    if 'coupon' in kwargs:
        return [
            int((1 - kwargs.get('coupon') * 0.01) * pay[i])
            for i in
            range(kwargs.get('count') if kwargs.get('count') <= len(pay) else len(pay))
        ]

    return None


help(use_coupon)
result = use_coupon(1000, 2000, 3000, coupon=50, count=100)

if result:
    print(result)
else:
    print('쿠폰이 없습니다.')










