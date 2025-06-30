class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed



    def drive(self):
        print(f"{self.brand} is driving at {self.speed} km/h")

my_car = Car("Toyota", 80)
my_car.drive()