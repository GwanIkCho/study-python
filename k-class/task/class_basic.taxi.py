# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

# 택시 객체 생성시 승객별로 돈과, 거리를 받아서 생성

# 거리에 따른 요금 계산 메소드 정의
# 거리에 따른 잔돈 계산 메소드 정의


class Texi:

    start_m = 5800
    start_km = 2
    add_m = 1000

    def __init__(self, money,last_km):
        self.money = money
        self.last_km = last_km


    def km(self):
        last_m = 0
        if self.last_km <= self.start_km:
            self.last_m = self.start_m
        else:
            self.last_m = self.start_m + ((self.last_km -self.start_km) * self.add_m)
        return last_m

    def change_money(self):
        return self.money - self.km()

# member1 = Texi(money=10000,last_km=3)
# member1.km()
# result = member1.money - member1.last_m
# print(f'받은돈 : {member1.money} 잔돈 : {result}')

# user = Texi(5000,5)
# print(user.money,user.last_km)

# class Texi:
#
#     start_m = 5800
#     start_km = 2
#     add_m = 1000
#
#     def __init__(self):
#         self.income = 0
#
#     def cost(self,money,last_km):
#         last_m = self.start_m
#         if self.last_km <= self.start_km:
#             self.last_m = self.start_m
#         else:
#             self.last_m = self.start_m + ((self.last_km -self.start_km) * self.add_m)
#         return last_m
#
#         self.income += self.income
#
#         def change_money():
#             return money - last_m
#
#
#         return last_m, change_money()
#
# taxi = Texi()
# taxi.cost(20000,1)
# print(taxi.income)

# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

# 1. 택시 객체 생성 시 승객 별로 돈과, 거리를 받아서 생성
# 2. 택시 객체 생성 시 택시 수익을 초기화한다.

# 1. 거리에 따른 요금 계산 메소드 정의
# 2. 거리에 따른 요금 계산 메소드 정의(승객의 돈과 거리를 전달받는다)
# 거리에 따른 잔돈 계산 메소드 정의

# 1.
# class Taxi:
#     default_fare = 5800
#     default_distance = 2
#     fare_per_km = 1000
#
#     def __init__(self, money, distance):
#         self.money = money
#         self.distance = distance
#
#     def calculate_fare(self):
#         cost = Taxi.default_fare
#         if self.distance > Taxi.default_distance:
#             cost += (self.distance - Taxi.default_distance) * Taxi.fare_per_km
#
#         return cost
#
#     def get_change(self):
#         return self.money - self.calculate_fare()
#
#
# taxi = Taxi(20000, 1)
# print(taxi.calculate_fare(), taxi.get_change())
#
# taxi = Taxi(30000, 10)
# print(taxi.calculate_fare(), taxi.get_change())


# 2.
class Taxi:
    default_fare = 5800
    default_distance = 2
    fare_per_km = 1000

    def __init__(self):
        self.income = 0

    def calculate_fare(self, money, distance):
        cost = Taxi.default_fare
        if distance > Taxi.default_distance:
            cost += (distance - Taxi.default_distance) * Taxi.fare_per_km

        self.income += cost

        def get_change():
            return money - cost

        return cost, get_change()


taxi = Taxi()
print(taxi.calculate_fare(20000, 1))
print(taxi.calculate_fare(30000, 10))
print(taxi.income)
