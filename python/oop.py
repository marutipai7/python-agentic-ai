class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(f"{self.brand} is driving at {self.speed} km/h")

#my_car = Car("Toyota", 80)
#my_car.drive()

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"The {self.name} makes a {self.species} sound.")

dog = Animal("Dog", "Woof")
cat = Animal("Cat", "Meow")

dog.speak()
cat.speak()