# class Magic:
#     def __init__(self, name):
#         self.name = name
#     # 초기화된 필드를 확인하고자 할때 사용한다.
#     def __str__(self):
#         return f'name : {self.name}'





    # def __str__(self):
    #     return f'{self.__repr__()}, __repr__() 사용됨.'

# 객체를 출력하면 항상 __repr__()가 자동으로 뒤에 붙는다.
# print(Magic().__repr__())
# 만약 해당 클래스에서 __str__()을 재정의했다면, __repr__()가 아닌 __str__()이 사용된다.
# print(Magic().__str__())
# 따라서, 생략해서 작성하면 __str__()이 붙게된다.
# print(Magic())



# magic = Magic('magic')
# print(magic)

class Student:
    def __init__(self, number, score):
        self.number = number
        self.score = score

    def __add__(self, other):
        #                      객체를받음
        return  self.score + other.score

    def __eq__(self, other):
        #  주소비교
        if self.__repr__() == other.__repr__():
            return True

        if isinstance(other, Student):
            # 값비교
            # isinstance(객체,타입): 전달한 객체가 전달한 타입일 경우True, 아니면 Fales
            return self.number == other.number

        return False



std1 = Student(1, 30)
std2 = Student(1 ,50)
std3 = Student(1,70)
total = std1.__add__(std3)
std1.__dict__.__getitem__('score')
print(std1.__dict__)
add = std1 + std2
print(total)
print(add)
print(std1 == std2)

















