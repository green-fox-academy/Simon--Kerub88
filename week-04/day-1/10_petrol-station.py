# Petrol Station
#
# Create Station and Car classes
# Station
#     gas_amount
#     refill(car) -> decreases the gasAmount by the capacity of the car and increases the cars gas_amount
# Car
#     gas_amount
#     capacity
#     create constriuctor for Car where:
#         initialize gas_amount -> 0
#         initialize capacity -> 100

class Station:
    def __init__(self, gas_amount):
        self.gas_amount = gas_amount

    def refill(self, car):
        self.gas_amount -= car.capacity
        car.gas_amount += car.capacity
        print(self.gas_amount)
        print(car.gas_amount)

class Car:
    def __init__(self, gas_amount = 0, capacity = 100):
        self.gas_amount = gas_amount
        self.capacity = capacity


tesla = Car()
Furioza = Station(500)

Furioza.refill(tesla)
