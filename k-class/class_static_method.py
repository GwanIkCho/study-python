class Student:
    status = '쉬는중'

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    @staticmethod
    def print_strat_time_of_study():
        print('9시 땡')
        Student.status = '공부중'




han = Student(0,0,0)
hong = Student(0,0,0)
print(Student.status)

Student.print_strat_time_of_study()
print(Student.status)

car = Car.translate_to_eng('Benz', '빨간색', 15000)
# car = Car('Benz', '빨간색', 15000)
print(car.color)