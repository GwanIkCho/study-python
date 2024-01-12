# # unpacking : 값을 풀어서 적는 것
# # def get_Total(number1,number2,number3):
# #     return number1+number2+number3
#
#
#
# # packing : 값을 묶어서 적는 것
# def get_Total(*numbers):
#     #  외부에서 전달받은 값들이 number(튜플)에 저장된다
#     print(type(numbers))
#     total = 0
#     for number in numbers:
#         total += number
#
#     return total
#
# # 여러개의 값을 ,로 구분하여 전달한다
# # total = get_Total(1,2,3,4,5)
# # print(total)
#
# numbers = [1,2,3,4,5]
# # 여러개의 값을 하나로 묶어서 전달하게되면 packing으로 인해ㅐ 첫번째 방에 통채로 들어가게된다.
# # 즉 결과는 다음과 같다 -> ([1,2,3,4,5],)
# # 따라서 내부의 요소를 각각 전달하고 싶다면, 앞에 *을 작성해야 한다.
# total = get_Total(*numbers)
# print(total)


# 국어, 영어, 수학 점수를 전달받은 뒤 총점으로 출력하는 함수
# 반드시 받아야하는 매개변수는 pcaking앞에 작성한다.
# def get_sum(*sum):
#     total = 0
#     for sum  in sum:
#         total += sum
#     return total

    # a,b,c = map(int,sum)
    # return a+b+c

# result = get_sum(30,30,30)
# print(result)

# 문자열에서 'A'가 몇개있는 지 검사하는 함수
# packing으로 제작하기

# def st(*stt):
#     result = []
#     count = 0
#
#     for a in stt:
#       for b in a:
#           if b == 'A':
#               count += 1
#       result.append(count)
#       count = 0
#
#     return result
#
# print(st('D','Asd','Ads'))




#     count = 0
#     for a in stt:
#         if 'A' == a:
#             count += 1
#     return count
#
# result = st(*'AAASDADAXAfsasD')
# print(result)