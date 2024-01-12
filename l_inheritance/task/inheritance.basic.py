# 인간(부모)
# 이름,나이
# 걷기(walk)
# '두발로 걷습니다. / 출력

# 원숭이(자식)
# 동물원,이름,나이,동물원이름
# 걷기(walk) 두발로 걷습니다. / 네발로 걷습니다.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def walk(self):
        print("두발로 걷습니다")

class Monkey(Person):
    def __init__(self, name, age, home):
        super().__init__(name, age)
        self.home = home
        self.name = name
        self.age = age

        self.name = name
        self.age = age
    def walk(self):
        super().walk()
        print('네발로 걷습니다.')


person = Person('cho',10)
print(person.name, person.age)
person.walk()
monkey = Monkey('m',1,'에버랜드')
print(monkey.name, monkey.age, monkey.home)
monkey.walk()