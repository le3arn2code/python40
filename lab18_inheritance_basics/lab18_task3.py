class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size=75):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def describe_car(self):
        super().describe_car()
        self.describe_battery()

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")


ecar = ElectricCar("Tesla", "Model 3", 2022, 100)
ecar.describe_car()
