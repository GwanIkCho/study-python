# def check(*,key,value):
#     for i in Bank.banks:
#         for user in i:
#             if user[key] == value:
#                 return user
#     return None
# class Bank:
#
#     total_bank = 3
#     banks = [[]for i in range(total_bank)]
#
#     def __init__(self,**kwargs):
#         self.name = kwargs.get('name')
#         self.account_number = kwargs.get('account_number')
#         self.phone = kwargs.get('phone')
#         self.pw = kwargs.get('pw')
#         self.money = kwargs.get('money')
#         self.object = self
#     @classmethod
#     def account_add(cls,bank_count, **kwargs):
#         user = [Shinhan,Kookmin,Kakao][bank_count-1](**kwargs)
#         cls.banks[bank_count-1].append(user.__dict__)
#
#
#     @staticmethod
#     def account_number_check(account_number):
#         return check(key='account_number',value=account_number)
#
#     @staticmethod
#     def phone_check(phone):
#         return check(key='phone',value=phone)
#
#
#     def deposit(self,cash):
#         self.money += cash
#
#     def withdraw(self, cash):
#         self.money -= cash
#
#     def balance(self):
#         return self.money
#
# class Shinhan(Bank):
#     def deposit(self,cash):
#         cash //= 2
#         super().deposit(cash)
#
# class Kookmin(Bank):
#     def withdraw(self,cash):
#         cash *= 1.5
#         super().withdraw(cash)
#
# class Kakao(Bank):
#     def balance(self):
#         self.money //=2
#         return super().balance()
#
# if __name__ == '__main__':
#     bank_menu = "1. 신한 은행\n" \
#                 "2. 국민 은행\n" \
#                 "3. 카카오 뱅크\n" \
#                 "4. 나가기\n"
#
#     menu = "1. 개설\n" \
#            "2. 입금\n" \
#            "3. 출금\n" \
#            "4. 잔액\n" \
#            "5. 계좌 번호 재설정\n" \
#            "6. 은행 선택 메뉴로 돌아가기\n"
#
#     owner_message = "예금주: "
#     account_number_message = "계좌번호: "
#     phone_message = "핸드폰 번호: "
#     password_message = "비밀번호(4자리): "
#     money_message = "예치금: "
#     deposit_message = "입금액: "
#     withdraw_message = "출금액: "
#     error_message = "다시 시도해주세요"
#
#
#     while True:
#         bank_choice = int(input(bank_menu))
#         if bank_choice == 4:
#             break
#
#         while True:
#             service = int(input(menu))
#             # 계좌개설
#             if service == 1:
#                 name = input(owner_message)
#                 while True:
#                     account_number = input(account_number_message)
#                     if Bank.account_number_check(account_number) is None:
#                         break
#                 while True:
#                     phone = input(phone_message)
#                     if Bank.phone_check(phone) is None:
#                         break
#
#                 while True:
#                     pw = input(password_message)
#                     if len(pw) == 4:
#                         break
#                 money = int(input(money_message))
#
#                 user = Bank.account_add(bank_choice,name=name,account_number=account_number,
#                             phone=phone,
#                             money=money,
#                             pw = pw)
#
#
#             # 입금
#             elif service == 2:
#                 account_number = input(account_number_message)
#                 user = Bank.account_number_check(account_number)
#                 if user is not None:
#                     if user['pw'] == input(password_message):
#                         deposit_money = int(input(deposit_message))
#                         user['object'].deposit(deposit_money)
#
#
#                 else:
#                     print(error_message)
#
#             # 출금
#             elif service == 3:
#                 account_number = input(account_number_message)
#                 user = Bank.account_number_check(account_number)
#                 if user is not None:
#                     if user['pw'] == input(password_message):
#                         withdraw_money = int(input(withdraw_message))
#                         user['object'].withdraw(withdraw_money)
#
#                 else:
#                     print(error_message)
#
#             # 잔액확인
#             elif service == 4:
#                 account_number = input(account_number_message)
#                 user = Bank.account_number_check(account_number)
#                 if user is not None:
#                     if user['pw'] == input(password_message):
#                         print(f'현재잔액 : {user["object"].balance()}')
#                 pass
#             elif service == 5:
#                 break
#
#
# class Calculator(object):
#
#
#
#     def __init__(self):
#         self.total = 0
#     def add(self,number):
#         self.total += number
#     def sub(self,number):
#         self.total -= number
#     def mul(self,number):
#         self.total *= number
#     def div(self,number):
#         self.total //= number
#     def reset(self):
#         self.total *= 0
#         return self
#
# calculator = Calculator()
#
# while True:
#     number = int(input("최초의 숫자를 입력하세요\n"))
#     calculator.add(number)
#     while True:
#
#         number = int(input("옵션을 선택하세요!\n"
#                            "1.더하기\n"
#                            "2.빼기\n"
#                            "3.곱하기\n"
#                            "4.나누기\n"
#                            "5.초기화\n"
#                            "6.나가기"))
#
#         if number == 1:
#             add_number = int(input("더하실 숫자를 입력하세요"))
#             calculator.add(add_number)
#             print(calculator.total)
#
#         elif number == 2:
#             sub_number = int(input("빼실 숫자를 입력하세요"))
#             calculator.sub(sub_number)
#             print(calculator.total)
#
#         elif number==3:
#             mul_number = int(input("곱하실 숫자를 입력하세요"))
#             calculator.mul(mul_number)
#             print(calculator.total)
#         elif number==4:
#             div_number = int(input("나누실 숫자를 입력하세요"))
#             calculator.div(div_number)
#             print(calculator.total)
#         elif number==5:
#             calculator.reset()
#             print('초기화가 완료되었습니다')
#
#         elif number==6:
#             break


def check(*,key,value):
    for i in Market.mart_list:
        for product in i:
            if product[key] == value:
                return product


    return None


class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        pass

class Market:

    total_mart = 2
    mart_list = [[]for i in range(total_mart)]


    def __init__(self, product, **kwargs):
        self.product = product
        self.stock = kwargs['stock']
        self.product = kwargs['product']
        self.price = kwargs['price']
        self.money = money


    @classmethod
    def display(cls,mart_choice,**kwargs):
        prod = [Amart,Bmart][mart_choice-1](**kwargs)
        cls.mart_list[mart_choice-1].append(prod.__dict__)
        return prod

    @staticmethod
    def product_check(product):
        return check(key='product', value=product)

    def sell(self,sell_count,product):
        self.stock -= sell_count
        self.money += product.price*sell_count
class Amart(Market):
    def sell(self,sell_count,product):
        self.stock -= sell_count
        self.money += product.price * sell_count * 0.9
        return super().sell(sell_count,product)




class Bmart(Market):
    def sell(self,sell_count, product):
        self.stock -= sell_count
        self.money += product.price * sell_count * 0.5
        return super().sell(sell_count, product)


while True:
    sell_market = int(input('관리할 매장을 골라주세요\n'
                            '1. A마트\n'
                            '2. B마트\n'
                            '3. 나가기\n'))

    if sell_market == 3:
        break

    else:
        print('다시 입력해주세요')


    while True:
        control_market = int(input('메뉴를 골라주세요\n'
                                   '1. 상품추가하기\n'
                                   '2. 상품수량설정\n'
                                   '3. 판매된 상품 처리하기\n'
                                   '4. 매출 현황\n'
                                   '5. 나가기\n'))

        if control_market == 1:
            product = input('상품명을 입력해주세요')
            while True:
                price = int(input('상품가격을 입려하세요'))
                if price >0 :
                    break
            while True:
                stock = int(input('수량을 입력하세요'))
                if stock > 0 :
                    break
            while True:




        elif control_market == 2:
            pass
        elif control_market == 3:
            pass
        elif control_market == 4:
            break

















