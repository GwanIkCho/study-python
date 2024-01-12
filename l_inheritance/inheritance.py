class A:
    def __init__(self, name):
        self.name = name

    def print_intro(self):
        print('A')

class B(A):
    def add(self, number1, number2):
        return number1 + number2
    def print_intro(self):
        # 부모의 메소드를 그대로 사용하고자 할때(선택 사할)
        super().print_intro()
        # 자식의 메소드에서 추가할 내용을 작성
        print('B')


a = A('kim')
b = B('cho')
print(b.name)
print(a.name)
b.print_intro()
print(b.add(1,2))