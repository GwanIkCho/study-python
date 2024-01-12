def check(*, key, value):
    for i in Market.mart_list:
        for product in i:
            if product[key] == value:
                return product
    return None


class Market:
    total_mart = 2
    mart_list = [[] for i in range(total_mart)]
    money = 0

    def __init__(self,**kwargs):
        self.product = kwargs['product']
        self.stock = kwargs['stock']
        self.price = kwargs['price']


    @classmethod
    def display(cls, mart_choice, **kwargs):
        prod = [Amart, Bmart][mart_choice - 1](**kwargs)
        cls.mart_list[mart_choice - 1].append(prod.__dict__)
        return prod

    @staticmethod
    def product_check(product):
        return check(key='product', value=product)

    def sell(self, sell_count, product):
        self.stock -= sell_count
        self.money += product.price * sell_count




class Amart(Market):
    def sell(self, sell_count, product):
        self.stock -= sell_count
        Market.money += product.price * sell_count * 0.9
        return super().sell(sell_count, product)


class Bmart(Market):
    def sell(self, sell_count, product):
        self.stock -= sell_count
        Market.money += product.price * sell_count * 0.5
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
                                   '2. 상품설정(가격, 수량)\n'
                                   '3. 판매된 상품 처리하기\n'
                                   '4. 매출 현황\n'
                                   '5. 상품리스트\n'
                                   '6. 나가기\n'))

        if control_market == 1:
            product = input('상품명을 입력해주세요')
            while True:
                price = int(input('상품가격을 입려하세요'))
                if price > 0:
                    break
            while True:
                stock = int(input('수량을 입력하세요'))
                if stock > 0:
                    break

                item = Market.display(product=product, price=price, quantity=stock)

        elif control_market == 2:
            product = input('상품명을 입력해주세요')
            iiii = Market.product_check(product)
            if iiii is not None:
                choice = int(input('바꾸실걸 설정해주세요\n'
                                   '1. 가격\n'
                                   '2. 수량\n'))
                if choice == 1:
                    new_price = int(input('새로운 가격을 입력해주세요'))
                    iiii['price'] = new_price
                    continue
                elif choice == 2:
                    new_stock = int(input('새로운 수량을 입력해주세요'))
                    iiii['stock'] = new_stock
                    continue
            else:
                print('상품명을 확인해주세여')

        elif control_market == 3:
            product = input('판매된 상품명을 입력해주세요')
            iiii = Market.product_check(product)
            if iiii is not None:
                sell_count = int(input('판매수량을 알려주세요'))
                if sell_count >0 :
                    Market.sell()
                else:
                    print('수량을 확인해주세요')
            pass
        elif control_market == 4:
            print()

        elif control_market == 5:
            print('asd')
            for i in Market.mart_list:
                for j in i:
                    print(f'{j["product"]}')
