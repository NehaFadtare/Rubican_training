from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def calculate_parking_fee(self,hours):
        pass

class Bike(Vehicle):
    def calculate_parking_fee(self,hours):
        fee = hours*20
        return f"total fee:{fee}"

class Car(Vehicle):
    def calculate_parking_fee(self,hours):
        fee = hours*50
        return f"total fee:{fee}"

class Truck(Vehicle):
    def calculate_parking_fee(self,hours):
        fee = hours*100
        return f"total fee:{fee}"


__name__=input("enter your name: ")
print(__name__)
__vehiNo__ = int(input("enter your vehivcal number: "))
print(__vehiNo__)
vehitype = input("enter type of your vehicle: ")
print(vehitype)
b1 = Bike()
c1 = Car()
t1 = Truck()
if vehitype=="bike":
    hours = int(input("how many hours: "))
    print(b1.calculate_parking_fee(hours))
elif vehitype == "car":
    hours = int(input("how many hours: "))
    print(c1.calculate_parking_fee(hours))
elif vehitype == "truck":
    hours = int(input("how many hours: "))
    print(t1.calculate_parking_fee(hours))
else:
    print("No such type found")



