# 회원의 주문 금액(pay)와 회원의 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# (선택사항) comprehension을 사용한다.






def discount(*args,**kwargs):
    result_list = []
    coupon, count = kwargs['coupon'], kwargs.get('count')
    for i in range(len(args)):
        if i > count:
            result_list.append(args[i])

        else:
           result_list.append(args[i] * (100-coupon)//100)
    return result_list



print(discount(100,200,300,coupon=50,count=10))