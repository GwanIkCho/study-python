import datetime


def Log_time(original_function):
    def logging(*args,**kwargs):
        self, other = args



        with open('log.txt', 'a', encoding='utf-8') as flie:
            result = original_function(self, other, **kwargs)
            now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


            if self.oper == '/':
                value, rest = result
                flie.write(f'{self.number}{self.oper}{other}= {value},{rest}\tKST{now}\n')
            else:
                flie.write(f'{self.number}{self.oper}{other}= {result}\tKST{now}\n')


            return result

    return logging

