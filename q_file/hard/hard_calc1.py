from q_file.hard.hard_log1 import Log_time


class Calculator:
    def __init__(self,number):
        self.number = number
        self.other = None

    def calc(self,oper,other):
        self.oper = oper
        oper_number = {'+':0 , '-':1, '*':2, '/':3}
        oper_list = [self.add,self.sub,self.mul,self.div]
        return oper_list[oper_number[oper]](other)

    @Log_time
    def add(self,other):
        return self.number + other

    @Log_time
    def sub(self,other):
        return self.number - other

    @Log_time
    def mul(self,other):
        return self.number * other

    @Log_time
    def div(self,other):
        return self.number // other, self.number%other