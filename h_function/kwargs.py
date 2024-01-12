# keyword arguments

# def introduce(**intro):
#     print(type(intro))
#     print(f'name : {intro["name"]}')
#
# info_dict = {'name':'cho'}
#
# introduce(name = 'cho')
# introduce(**info_dict)


# 주문 가격과 주문한 회원의 정보 출력
# def order_info(*args, **kwargs):
#     total = 0
#     for i in args:
#         total += 1
#
#     print(f'{kwargs["name"]}님의 총 주문가격은 {total}원입니다')
#
# order_info(300,200,100, name='cho')

# 국어, 영어, 수학 점수의 평균 구하기
# 사용자가 원하는 자리수에서 반올림해준다.
# 자리수를 받지 않았다면 기본값을 리턴한다.


# def average(**kwargs):
#     kor = kwargs['kor']
#     eng = kwargs['eng']
#     math = kwargs['math']
#     result = (kor + eng + math) / 3
#     if "round" in kwargs:
#         return round(result,kwargs['round'])
#     return result
#
# print(average(kor=100, eng=30, math=21, round= 3))

# 반드시 key와 함께 사용하고자 할때에는 매갭ㄴ수를 시작울 *로 한다.
# def average(*, kor,eng,math):
#     return (kor+eng+math) /3
#
# print(average(kor= 10,eng=20,math=30))
