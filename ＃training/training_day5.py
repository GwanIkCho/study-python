def check(**kwargs):
    if 'account_number' in kwargs:
        value = kwargs.get('account_number')
        for i in range(Bank.total_count):
            for user_info in Bank.banks[i]:
                if user_info.account_number == value:
                    return True
        return False
    else:
        value = kwargs.get('phone')
        for i in range(Bank.total_count):
            for user_info in Bank.banks[i]:
                if user_info.phone == value:
                    return True
        return False


class Bank:
    total_count = 3
    banks = [[] for _ in range(total_count)]

    def __init__(self, **kwargs):
        self.owner = kwargs['owner']
        self.account_number = kwargs['account_number']
        self.phone = kwargs['phone']
        self.password = kwargs['password']
        self.money = 0
        bank_choice = kwargs['bank_choice']
        Bank.banks[bank_choice - 1].append(self)

    @classmethod
    def open_account(cls, **kwargs):
        bank_choice = kwargs['bank_choice']
        if bank_choice == 1:
            return ShinHan(**kwargs)
        elif bank_choice == 2:
            return KookMin(**kwargs)
        return KaKao(**kwargs)

    @staticmethod
    def check_account_number(account_number):
        return check(account_number=account_number)

    @staticmethod
    def check_phone(phone):
        return check(phone=phone)

    def deposit(self, amount):
        self.money += amount

    def withdraw(self, amount):
        self.money -= amount

    def balance(self):
        return self.money

    def __str__(self):
        return f'예금주: {self.owner}\n\
                계좌번호: {self.account_number}\n\
                핸드폰번호: {self.phone}\n\
                비밀번호: {self.password}\n\
                통장잔고: {self.money}'

    @staticmethod
    def login(**kwargs):
        bank_choice = kwargs['bank_choice']
        account_number = kwargs['account_number']
        password = kwargs['password']
        for user_info in Bank.banks[bank_choice - 1]:
            if user_info.account_number == account_number and \
                    user_info.password == password:
                return user_info
        return None

    @staticmethod
    def find_account_by_phone(bank_choice, phone):
        for user_info in Bank.banks[bank_choice - 1]:
            if user_info.phone == phone:
                return user_info
        return None

    @staticmethod
    def update_account_number(user_info, new_account_number):
        if check(account_number=new_account_number):
            return False
        user_info['account_number'] = new_account_number
        return True


class ShinHan(Bank):
    def deposit(self, amount):
        amount = int(amount * 0.5)
        super().deposit(amount)


class KookMin(Bank):
    def withdraw(self, amount):
        amount = int(amount * 1.5)
        super().withdraw(amount)


class KaKao(Bank):
    def balance(self):
        self.money //= 2
        return super().balance()


if __name__ == '__main__':
    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"

    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 계좌번호 찾기\n"\
           "6. 은행 선택 메뉴로 돌아가기\n"

    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    new_account_number_message = "새로운 계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"
    account_exist_message = "중복된 계좌번호입니다."
    phone_exist_message = "중복된 전화번호입니다."
    update_account_result_message = "변경되었습니다."


    while True:
        # 은행 메뉴
        bank_choice = int(input(bank_menu))
        if bank_choice == 4:
            break
        while True:
            # 서비스 메뉴
            service = int(input(menu))
            if service == 1:
                owner = input(owner_message)
                while True:
                    account_number = input(account_number_message)
                    if not check(account_number=account_number):
                        break
                while True:
                    phone = input(phone_message)
                    if not check(phone=phone):
                        break
                while True:
                    password = input(password_message)
                    if len(password) == 4:
                        break
                Bank.open_account(bank_choice=bank_choice,
                                  owner=owner,
                                  account_number=account_number,
                                  phone=phone,
                                  password=password)
            elif service == 2:
                account_number = input(account_number_message)
                password = input(password_message)
                user_info = Bank.login(bank_choice=bank_choice, account_number=account_number, password=password)
                if not user_info:
                    print(error_message)
                    continue
                deposit_amount = int(input(deposit_message))
                user_info.deposit(deposit_amount)
            elif service == 3:
                account_number = input(account_number_message)
                password = input(password_message)
                user_info = Bank.login(bank_choice=bank_choice, account_number=account_number, password=password)
                if not user_info:
                    print(error_message)
                    continue
                withdraw_amount = int(input(withdraw_message))
                if withdraw_amount * (1.5 if bank_choice == 2 else 1) <= user_info.money:
                    user_info.withdraw(withdraw_amount)
                else:
                    print(error_message)
            elif service == 4:
                account_number = input(account_number_message)
                password = input(password_message)
                user_info = Bank.login(bank_choice=bank_choice, account_number=account_number, password=password)
                if not user_info:
                    print(error_message)
                    continue
                print(f"잔액: {user_info.balance()}원")
            elif service == 5:
                phone = input(phone_message)
                user_info = Bank.find_account_by_phone(bank_choice, phone)
                if not user_info:
                    print(error_message)
                    continue
                while True:
                    new_account_number = input(new_account_number_message)
                    if Bank.update_account_number(user_info, new_account_number):
                        print(update_account_result_message)
                        break
                    print(account_exist_message)
            else:
                break