class Car:
    wheels = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is now driving.")

car = Car("Ford", "Mustang")

print(f"Brand: {car.brand}")
print(f"Model: {car.model}")
print(f"Number of wheels: {Car.wheels}")
