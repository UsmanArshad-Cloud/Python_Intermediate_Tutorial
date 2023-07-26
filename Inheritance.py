class Car:
    def __init__(self, SeatingCapacity, Speed, make, model):
        self.SeatingCapacity = SeatingCapacity
        self.Speed = Speed
        self.make = make
        self.model = model
        print("Constructor of Class")

    def __str__(self):
        return f"This car has seating capacity of {self.SeatingCapacity} and Speed of {self.Speed}"

    def __del__(self):
        print("Deleting Car")
class FuelCar(Car):
    def __init__(self,SeatingCapacity,Speed,Make,Model,FuelCapacity):
        print("Constuctor of Fuel Car")
        super().__init__(SeatingCapacity,Speed,Make,Model)
        self.FuelCapacity=FuelCapacity
    def __del__(self):
        print("Deleting Fuel Car")
class ElectricCar(Car):
    def __init__(self,SeatingCapacity,Speed,Make,Model,BatteryCpacity):
        print("Constructor of Electric Car")
        super().__init__(SeatingCapacity,Speed,Make,Model)
        self.BatteryCapacity=BatteryCpacity
    def __del__(self):
        print("Deleting Electric Car")

EC=ElectricCar(2,300,"Ferrari",2023,50)
FuelCar(4,300,"Land Cruiser",2023,50)