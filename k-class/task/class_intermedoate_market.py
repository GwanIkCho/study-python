# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class User:
#     def __init__(self,u_name,age,discount,money):
#         self.u_name = u_name
#         self.age = age
#         self.discount = discount
#         self.money = money
#
# class Market:
#     def __init__(self,item):
#         self.item = item
#     def sell(self, user):
#         self.user = user
#         self.item.price - (100-self.item.discount // 100)
#
#
#
#
# Item("snack",1000)
# User("cho",20,10,10000)
# Market('snack',40)
#
# print()


# 상품
# 상품명, 가격
# 상품의 정보를 print()로 출력하는 함수

# 마켓
# 상품, 재고
# 손님 한 명에게 한 개의 상품을 판매한다.
# 판매 시 손님의 할인율을 적용하여 판매한다.

# 손님
# 이름, 나이, 할인율, 잔액

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self,name,age,discount, money = 0):
        self.name = name
        self.money = money
        self.age = age
        self.discount = discount
class Market:
    def __init__(self,products, stock):
        self.products = products
        self.stock = stock

    def sell(self, customer):

        customer.money -= self.products.price * (1 - customer.discount * 0.01)
        self.stock -= 1

product = Product("사과", 3000)
customer = Customer("cho", 20, 30, money=10000)
market = Market(product, stock=40)
market.sell(customer)
print(market.stock)
print(customer.money)






