import datetime


def Log_time(original_function):
    def logging(*args,**kwargs):
        self,other = args
        now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        result = original_function(*args,**kwargs)
        if self.oper == '/':
            a, b = result
            print(f'{self.number}{self.oper},{other} = {a}, {b} \tKST{now}')

        else:
            print(f'{self.number}{self.oper},{other} = {result} \tKST{now}')
        return result

    return logging


