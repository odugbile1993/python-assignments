# Assignment 1: Design Your Own Class (Smartphone Example) 🏗️


class Device:

    def __init__(self, brand, model):

        self.brand = brand

        self.model = model


    def device_info(self):

        return f"{self.brand} {self.model}"


class Smartphone(Device):  # Inheriting from Device

    def __init__(self, brand, model, storage):

        super().__init__(brand, model)

        self.storage = storage


    def device_info(self):  # Polymorphism example

        return f"{self.brand} {self.model} with {self.storage}GB storage"


    def call(self, number):

        print(f"Calling {number}... 📞")


# Creating Smartphone objects
phone1 = Smartphone("Apple", "iPhone 14", 256)

phone2 = Smartphone("Samsung", "Galaxy S23", 128)


print(phone1.device_info())

print(phone2.device_info())

phone1.call("+123456789")



# Activity 2: Polymorphism Challenge 🎭


class Vehicle:

    def move(self):

        print("Vehicle is moving")


class Car(Vehicle):

    def move(self):

        print("Driving 🚗")


class Plane(Vehicle):

    def move(self):

        print("Flying ✈️")


class Boat(Vehicle):

    def move(self):

        print("Sailing 🚢")


# List of different vehicles
vehicles = [Car(), Plane(), Boat()]


# Polymorphism in action
for v in vehicles:

    v.move()
