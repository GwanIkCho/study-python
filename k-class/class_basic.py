# 동물
# 이름, 나이,성별, 음식개수. 체력개수
# 먹기, 산책하기



class Animal:

    def __init__(self,name,age,gender,feed_count=1,life=1):
        self.name = name
        self.age = age
        self.gender=gender
        self.feed_count=feed_count
        self.life= life

    # 음식 한개를 소모 체력 1 흭득
    def eat(self):
        self.feed_count-= 1
        self.life +=1

    # 체력 1개를 소모 음식 1개를 흭득
    def walk(self):
        self.feed_count += 1
        self.life -= 1

tiger = Animal(name='호랭이', age=10 ,gender='수컷')
lion = Animal(name='사자', age=20 ,gender='암컷')

tiger.eat()
lion.walk()

print(tiger.name, tiger.age, tiger.gender, tiger.feed_count, tiger.life)
print(lion.name,lion.age,lion.gender,lion.feed_count,lion.life)