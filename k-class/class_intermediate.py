class car:
    # 정적변수 (static variable)
    wheel = 4

    def __init__(self,brand = '',color = '',price = 0):
        self.brand = brand
        self.color = color
        self.price = price

    def engine_start(self):
        print(self.brand+ '시동켜짐')

    def engine_end(self):
        print(self.brand + '시동꺼짐')


# mom_car = car('benz','black',15000)
# daddy_car = car('bmw','blue',8800)

# mom_car.engine_start()
# daddy_car.engine_start()
# print(car.wheel)
# car.wheel = 6
#
# print(mom_car.wheel)

cars = [car,car]
mom_car = cars[0]()
daddy_car = cars[1]()

print(cars[1])

