# # 순서 고정을 위해 *,key, value
# # 핸드폰, 계좌 번호 검사가능
# # 정확히 어떤것을 검사할지는 전달받은key로 가능
# def check(*,key, value) ->dict:
#     # 은행들중(DB에 있는 여러개의 은행중)에서 은행의 정보를 받고
#     for bank in Bank.banks:
#             # 각 은행에서 회원의 정보를 찾고
#         for user in bank:
#                 # 유저의 키값이 value랑 같은지 확인
#             if user[key] == value:
#                 # 맞다면 정보를 올림
#                 return user
#     # 정보가 틀립니다.
#     return None
#
#
# class Bank:
#     # 가지고 있는 은행을 나타낸다. (은행이 늘어나면 카운트 늘리기 가능해서 따로빼둠)
#     total_count = 3
#     # 은행들을 리스트에 담어둠
#     # 은행들이있는 각각의 리스트 안에다가 고객정보를 입력하면 그 주소값을 입력
#     # total count만큼 돌려서 은행의 수 만큼 리스트 안에 리스트 추가해줌
#     banks = [[]for i in range(total_count)]
#
#     # 알아야 하는 고객정보들 담음
#     def __init__(self, **kwargs):
#         self.name = kwargs['name']
#         self.account_number = kwargs['account_number']
#         self.password = kwargs['password']
#         self.phone = kwargs['phone']
#         self.money = money
#         # 각 회원의 object 필드에는 필드의 주소값이 담긴다.
#         self.object = self
#
#
#     # 어떠한 은행에서 개설하는지 bank_choice로 전달받는다.
#     @classmethod
#     # bank_count는 bank에서 어디 인덱스에 있는지 알기위해 적고 kwargs는 그 인덱스에 정보를 담기위해 작성해야함
#     def opne_account(cls, bank_choice, **kwargs):
#         # bank는 아래 은행들이 있는 은행에 (banks) bank_choice 신 국 카 가각 1.2.3이면 인덱스는 0부터니 -1하고 정보입력
#         # 회원이 어떤 은행에서 개설하는지 알 수 없다. 전달받은 bank_choice를 통해
#         bank = [Shinhan, Kookmin, Kakao][bank_choice -1](**kwargs)
#         # check함수에서 원하는 key로 회원의 정보를 찾기 위해
#         cls.banks[bank_choice -1].append(bank.__dict__)
#         return bank
#
#     @staticmethod
#     def check_account_number(account_number) -> dict:
#         # 검사할 번호를 받고 위로 체크에 담아주면 위에있는 검사 실행
#         return check(key ='account_number', value= account_number)
#
#     @staticmethod
#     def check_phone(phone)-> dict:
#         # 검사할 번호를 받고 위에 체크에 담아서 검사
#         return check(key ='phone', value= phone)
#
#     def deposit(self, cash):
#         # 돈(cash)입력하면 입력값 money에 담김
#         self.money += cash
#
#     def withdraw(self, cash):
#         # 위와 반대로 빠짐
#         self.money -= cash
#     def balance(self):
#         # 현재 money값을 리턴해주면서 보여줌
#         return self.money
#
#     def __str__(self):
#         return (f'{self.name}, '
#                 f'{self.account_number}, '
#                 f'{self.phone}, '
#                 f'{self.password}, '
#                 f'{self.money}')
#
#
#
# class Shinhan(Bank):
#     def deposit(self, cash):
#         # 부모쪽으로 넘어가기전에 cash반토만 해주고 입금해줌
#         cash //= 2
#         # 부모 그대로 계승하겠다는 뜻
#         super().deposit(cash)
#
# class Kookmin(Bank):
#     def withdraw(self, cash):
#         # 돈을뺄때는 그 금액의 1.5배를 필요로 하게 만들어줌(금액설정)
#         cash *= 1.5
#         # 부모쪽 계승하겠다고 알림
#         super().withdraw(cash)
# class Kakao(Bank):
#     def balance(self):
#         # 자신이 가지고 있는 돈을 반으로 나눠줌
#         self.money //2
#         # 부모꺼 계승해옴
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
#            '5. 계좌번호 바꾸기\n'\
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
#     add_message1 ='핸드폰 번호 입력해주세용'
#     add_message2 ='비밀번호 입력해주세요'
#     add_message3 ='새로운 계좌를 적어주세요'
#     # d
#     while True:
#         # 먼저 은행 or 탈출 선택권을 줌 은행선택한거는 위랑 연동
#         bank_choice = int(input(bank_menu))
#         # 4번은 나가기임
#         if bank_choice == 4:
#             break
#
#         if bank_choice < 1 or bank_choice > len(Bank.banks):
#             continue
#             # 탈 - 출
#
#
#         while True:
#             #이제서비스 만들어줘야함
#             service = int(input(menu))
#             # 1번 계좌만들기
#             if service == 1:
#                 # 만드는 사람 이름 받아주고
#                 name = input(owner_message)
#                 # 정확한? 조건을 어기지 않는 값 입력할때까지 탈출불가상태 만들기
#                 while True:
#                     # 희망하는 계좌번호를 받아줍니다
#                     account_number = input(account_number_message)
#                     # 계좌를 체크에 넣어서 번호가 있는지 확인하고 없으면 통-과
#                     if not Bank.check_account_number(account_number):
#                         break
#                 while True:
#                     # 희망? 하는 번호를 입력하고
#                     phone = input(phone_message)
#                     # 중복이 없다면 통-과
#                     if not Bank.check_phone(phone=phone):
#                         break
#                 while True:
#                     # 희망하는 비밀번호를 받고
#                     password = input(password_message)
#                     # 4자리가 아니면 탈출 불가
#                     if len(password) == 4:
#                         break
#
#                 # 예치금 넣을건가요? 물어봄
#                 money = int(input(money_message))
#
#
#                 # 통장 만드는 곳에 담아서 완성시켜주기
#                 user = Bank.opne_account(bank_choice=bank_choice,
#                                    name=name,
#                                   account_number=account_number,
#                                   phone=phone,
#                                   password=password)
#                 print(user)
#             # 2번은 입금
#             elif service == 2:
#                 # 입금할 계좌번호 받고
#                 # 개설한 은행에서만 입금 가능
#                 account_number = input(account_number_message)
#                 # 계좌번호 체크 겸 유저에 담아둠
#                 user = Bank.check_account_number(account_number)
#                 if isinstance(user['object'], Shinhan):
#                     if bank_choice != 1:
#                         print('개설한 은행에서만 입금 서비스를 사용할수 있습니다.')
#                         continue
#                  # 이게 가수?가 아니라면
#                 if user is not None:
#                     #  비밀번호를 받아서 맞는지 확인해봅니다
#                     if user['password'] == input(password_message):
#                         # 입금 얼마나 할건지 받아주고
#                         deposit_money = int(input(deposit_message))
#                         #  요밑에는 위에 object - self 해주고 위에 담는걸 새로 생성하고 뒤에거 담아줌
#                         user['object'].deposit(deposit_money)
#                         continue
#
#                 else:
#                     # 계좌번호 이상하거나 그러면 나옴
#                     print(error_message)
#             # 3번은 출금
#             elif service == 3:
#                 # 계좌번호 받고
#                 account_number = input(account_number_message)
#                 # 있는지 확인하고 유저에 담아주고
#                 user = Bank.check_account_number(account_number)
#                 #  이게 없는게 아니라면
#                 if user is not None:
#                     # 비밀번호 입력받고
#                     if user['password'] == input(password_message):
#                         # 출금할 금액을 물어보고
#                         withdraw_money = int(input(withdraw_message))
#                         # withdraw_money는 유저가 국민에 담겨있다면 1.5배로 가야하며 아니면 그냥 1로 간다.
#                         if withdraw_money * (1.5 if isinstance(user['object'], Kookmin) else 1) <= user['money']:
#                             user['object'].withdraw(withdraw_money)
#                             continue
#                         else:
#                             # 잔액부족!
#                             print(error_message)
#                 # 통장이 없는디?
#                 else:
#                     print(error_message)
#             # 잔액조회
#             elif service == 4:
#                 # 언제나처럼 평화롭게 계좌받고
#                 account_number = input(account_number_message)
#                 # 계좌 있는지 확인하고 유저에 담고
#                 user = Bank.check_account_number(account_number)
#                 # 번호가 있고 이게 담겨있다면
#                 if user is not None:
#                     # 비밀번호는 한번확인해주고
#                     if user['password'] == input(password_message):
#                         print(f' {user["object"].balance()}')
#                         continue
#                 else:
#                     print(error_message)
#
#             # 계좌 번호 재설정
#             # 핸드폰 번호, 비밀번호 입력 후
#             # 정확하면, 해당 회원의 계좌번호 재설정(다시 입력받기)
#             elif service == 5:
#                 # 먼저 핸드폰 번호를 받아주고
#                 phone = input(add_message1)
#                 # 검사하면서 유저 정보를 받아주고
#                 user = Bank.check_phone(phone)
#                 # 유저가 정확한 값을 가지고있는지 확인
#                 if user is not None:
#                     # 유저 비밀번호 = 입력한 비밀번호 같은지 확인
#                     if user['password'] == input(add_message2):
#                         while True:
#                             account_number = input(account_number_message)
#                             if Bank.check_account_number(account_number) is None:
#                                 break
#                             user['account_number'] = account_number
#                     print('핸드폰 번호 혹은 비밀번호를 다시 확인해주세요.')
#                     # 새로운 계좌번호를 받고
#                     new_account_number = input(add_message3)
#                     # 유저에다가 적용시켜 줍니다.
#                     user['account_number'] = new_account_number
#                     continue
#                 else:
#                     print(error_message)
#
#             #  안한거 - 새로받은 계좌에 중복검사 추가해야합니다.
#             #  비밀번호 받는것도 if문으로 받아야합니다.
#
#
#             elif service == 6:
#                 break
#
#             else:
#                 print(error_message)

total_mart = 2
mart_list = [[] for i in range(total_mart)]
product_dict = {'product': 1, 'stock' : 1}
mart_list[0].append(product_dict)

for i in mart_list:
    for product in i:
        print(product['product'])

