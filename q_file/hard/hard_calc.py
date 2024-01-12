from q_file.hard.hard_log import Log_time


class Calculator:
    def __init__(self, number):
        self.number = number
        self.oper = None

    def calc(self,other,oper):
        self.oper = oper
        oper_number = {'+': 0, '-': 1,'*': 2,'/': 3 }
        oper_list = [self.add, self.__sub__, self.__mul__, self.__floordiv__]
        return oper_list[oper_number[oper]](other)

    @Log_time
    def add(self, other):
        return self.number + other

    @Log_time
    def __sub__(self, other):
        return self.number - other

    @Log_time
    def __mul__(self, other):
        return self.number * other

    @Log_time
    def __floordiv__(self, other):
        return self.number // other, self.number % other