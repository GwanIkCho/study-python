# # # # # 상품
# # # # # 상품명, 가격
# # # # # 상품의 정보를 print()로 출력하는 함수
# # # #
# # # # # 마켓
# # # # # 상품, 재고
# # # # # 손님 한 명에게 한 개의 상품을 판매한다.
# # # # # 판매 시 손님의 할인율을 적용하여 판매한다.
# # # #
# # # # # 손님
# # # # # 이름, 나이, 할인율, 잔액
# # # #
# # # #
# # # # class Item():
# # # #     def __init__(self, name, price):
# # # #         self.name = name
# # # #         self.price = price
# # # #
# # # # class User():
# # # #     def __init__(self,name,age,discount,money=0):
# # # #         self.name = name
# # # #         self.age = age
# # # #         self.discount = discount
# # # #         self.money = money
# # # #
# # # # class Market():
# # # #     def __init__(self,item,stock):
# # # #         self.item = item
# # # #         self.stock = stock
# # # #     def sell(self,user):
# # # #         user.money -= self.item.price * (1-user.discount*0.01)
# # # #         self.stock -= 1
# # # #
# # # # item = Item('과자',10000)
# # # # user = User('cho',10,20,10000)
# # # # market = Market(item,20)
# # # # market.sell(user)
# # # # print(market.stock)
# # # # print(user.name, user.money)
# # #
# # # # 학교
# # # # 이름, 지역, 학생 수, 선생님 수
# # # # 학교 정보 출력 메소드
# # #
# # # # 선생님
# # # # 이름, 과목, 학교
# # # # 선생님이 추가될 때마다 선생님 수 1증가
# # # # 준비된 학생들에게 해당 과목을 가르치면 학생들의 능력치 1증가
# # # # 선생님 정보 출력 메소드
# # #
# # # # 학생
# # # # 이름, 학년(grade), 학교, 능력치(초기값: 0), 담임 선생님
# # # # 학생이 추가될 때마다, 학생 수 1증가
# # # # 학생 정보 출력 메소드
# # #
# # # # class School:
# # # #     def __init__(self, name, adress, student_cont, teacher_cont):
# # # #         self.name = name
# # # #         self.adress = adress
# # # #         self.student_cont = student_cont
# # # #         self.teacher_cont = teacher_cont
# # # #
# # # # class Student:
# # # #     def __init__(self, name, grade, school, teacher, ability=0):
# # # #         self.name = name
# # # #         self.school = school
# # # #         self.grade = grade
# # # #         self.teacher = teacher
# # # #         self.ability = ability
# # # #         self.school.student_cont += 1
# # # #     def
# # # #
# # # # class Teacher:
# # # #     def __init__(self, name, math, school):
# # # #         self.name = name
# # # #         self.math = math
# # # #         self.school = school
# # # #         self.school.teacher_cont += 1
# # #
# # #
# # # # '택시'에서 승객들에게 공통적으로 적용되는 자료
# # # # - 기본 요금 : 5800원
# # # # - 기본 주행 거리 : 2km
# # # # - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원
# # #
# # # # 택시 객체 생성시 승객별로 돈과, 거리를 받아서 생성
# # #
# # # # 거리에 따른 요금 계산 메소드 정의
# # # # 거리에 따른 잔돈 계산 메소드 정의
# # #
# # #
# # # class Taxi:
# # #     start_money = 5800
# # #     start_km = 2
# # #     add_money = 1000
# # #     last_money = 0
# # #     def __init__(self):
# # #         self.income = 0
# # #     def get_money(self,money,km):
# # #         cost = Taxi.start_money
# # #         if km > Taxi.start_km:
# # #             cost += (km - Taxi.start_km) * Taxi.add_money
# # #         self.income += cost
# # #
# # #         def get_change():
# # #             return money - cost
# # #
# # #
# # # user = Taxi()
# # # print(user.get_money(10000,4))
# # # print(user.income)
# #
# # # 학교
# # # 이름, 지역, 학생 수, 선생님 수
# # # 학교 정보 출력 메소드
# # # 선생님
# # # 이름, 과목, 학교
# # # 선생님이 추가될 때마다 선생님 수 1증가
# # # 준비된 학생들에게 해당 과목을 가르치면 학생들의 능력치 1증가
# # # 선생님 정보 출력 메소드
# # # 학생
# # # 이름, 학년(grade), 학교, 능력치(초기값: 0), 담임 선생님
# # # 학생이 추가될 때마다, 학생 수 1증가
# # # 학생 정보 출력 메소드
# #
# # class School:
# #     def __init__(self,name,adress,student_count = 0,teacher_count = 0):
# #         self.name = name
# #         self.adress = adress
# #         self.student_count = student_count
# #         self.teacher_count = teacher_count
# #
# #     def print_info(self):
# #         print(self.name,self.adress,self.student_count,self.teacher_count)
# #
# # class Teacher:
# #     def __init__(self,name,math,school):
# #         self.name = name
# #         self.math = math
# #         self.school = school
# #         self.school.teacher_count += 1
# #
# #     def print_info(self):
# #         print(self.name,self.math,self)
# #         self.school.print_info()
# #
# #     def teach(self,students):
# #         for student in students:
# #             student.ability += 1
# #
# # class Student:
# #     def __init__(self,name, grade, school, teacher, ability = 0):
# #         self.name = name
# #         self.grade = grade
# #         self.school = school
# #         self.teacher = teacher
# #         self.ability = ability
# #         self.school.student_count += 1
# #
# #     def print_info(self):
# #         print(self.name,self.grade,self.school,self.teacher,self.ability)
# #         self.school.print_info()
# #         self.teacher.print_info()
# #
# # school = School('영동고등학교', '서울')
# # teacher = Teacher('한동석', '컴퓨터', school)
# # students = [
# #     Student('홍길동', 1, school, teacher),
# #     Student('이순신', 1, school, teacher),
# #     Student('장보고', 2, school, teacher)
# # ]
# #
# #
# # print(students)
#
# # 인간(부모)
# # 이름,나이
# # 걷기(walk)
# # '두발로 걷습니다. / 출력
#
# # 원숭이(자식)
# # 동물원,이름,나이,동물원이름
# # 걷기(walk) 두발로 걷습니다. / 네발로 걷습니다.
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         print('두발로 걷습니다.')
#
# class Monkey(Person):
#     def __init__(self, name, age, zoo):
#         super().__init__(name, age)
#         self.zoo = zoo
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         super().walk()
#         print('네발로 걷습니다.')
#
# person = Person('cho', 10)
# print(person.name, person.age)
# person.walk()
# monkey = Monkey('몽', 1, 'zoo')
# print(monkey.name, monkey.age, monkey.zoo)
# monkey.walk()

# PartTimer

# '모든 직원'에 공통적으로 적용되는 내용
# - 시급
# - 직원수

# '각 직원'별로 적용되는 내용
# - 별명
# - 근무지(기본값: '청담동')
# - 급여 총액(초기값: 0, 생성자로 초기화 불가능)

# 직원 급여 계산
#   '근무 시간 + 상여금'에 따른 직원 급여 계산
#   '상여금'은 지정 하지 않으면 0 으로 처리

# class PartTime:
#     hour_pay = 10000
#     user_count = 0
#     def __init__(self, name, adress = '청담동'):
#         self.name = name
#         self.adress = adress
#         self.cost = 0
#         PartTime.user_count += 1
#
#     def get_pay(self,hour,add = 0):
#         cost = hour * self.hour_pay + add
#         self.user_count += cost
#
#         return cost
#
# cho = PartTime('cho')
# print(cho.name, cho.adress)
# result =cho.get_pay(5, 5000)
# print(result)

# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

# 1. 택시 객체 생성 시 승객 별로 돈과, 거리를 받아서 생성
# 2. 택시 객체 생성 시 택시 수익을 초기화한다.

# 1. 거리에 따른 요금 계산 메소드 정의

# class Taxi:
#
#     start_m = 5800
#     start_km = 2
#     add = 1000
#
#     def __init__(self):
#         self.income = 0
#
#     def pay(self,money,km):
#         cost = Taxi.start_m
#         if km > self.start_km:
#             cost +=  ((km - Taxi.start_km) * Taxi.add)
#
#         def change():
#             return money - cost
#
#         return cost, change()
#
# taxi = Taxi()
# print(taxi.pay(10000,3))

# 상품
# 상품명, 가격
# 상품의 정보를 print()로 출력하는 함수

# 마켓
# 상품, 재고
# 손님 한 명에게 한 개의 상품을 판매한다.
# 판매 시 손님의 할인율을 적용하여 판매한다.

# 손님
# 이름, 나이, 할인율, 잔액

# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class User:
#     def __init__(self, name, age, discount, money = 0):
#         self.name = name
#         self.age = age
#         self.discount = discount
#         self.money = money
# class Market:
#     def __init__(self, item, stock):
#
#         self.item = item
#         self.stock = stock
#
#     def sell(self, user):
#         user.money -= self.item.price * ((100-user.discount) // 100)
#         self.stock -= 1
#
#
#
# item = Item('사과',10000)
# user = User('cho', 10, 10, 10000)
# market = Market(item,40)
#
# print(item.name, item.price)
# market.sell(user)
# market.sell(user)
# print(market.stock)
# print(user.money)

# 학교
# 이름, 지역, 학생 수, 선생님 수
# 학교 정보 출력 메소드
# 선생님
# 이름, 과목, 학교
# 선생님이 추가될 때마다 선생님 수 1증가
# 준비된 학생들에게 해당 과목을 가르치면 학생들의 능력치 1증가
# 선생님 정보 출력 메소드
# 학생
# 이름, 학년(grade), 학교, 능력치(초기값: 0), 담임 선생님
# 학생이 추가될 때마다, 학생 수 1증가
# 학생 정보 출력 메소드


class School:
    def __init__(self, name, adress, student_connt = 0, teacher_connt = 0):
        self.name = name
        self.adress = adress
        self.student_connt = student_connt
        self.teacher_connt = teacher_connt
    def info(self):
        print(self.name, self.adress, self.student_connt, self.teacher_connt)



class Teacher:
    def __init__(self, name, math, school):
        self.name = name
        self.math = math
        self.school = school
        self.school.teacher_connt += 1

    def teach(self,students):
        for student in students:
            student.ability += 1

    def info(self):
        print(self.name, self.math, self.school)
        self.school.info()

class Student:
    def __init__(self, name, grade, school, teacher, ability = 0):
        self.name = name
        self.grade = grade
        self.school = school
        self.teacher = teacher
        self.ability = ability
        self.school.student_connt += 1

    def info(self):
        print(self.name, self.grade, self.school,self.teacher,self.ability)


school = School('잠실고', '잠실')
teacher = Teacher('cho', '수-학',school)
student = Student('kim', 1, school, teacher)
student = Student('pack', 1, school, teacher)

student.info()
# print(student.name, student.grade, student.school, student)
# print(Student.info())