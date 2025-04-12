class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_info(self):
        return f"Brand: {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_info(self):
        return f"{super().show_info()}, Model: {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def show_info(self):
        return f"{super().show_info()}, Battery: {self.battery_size} kWh"

tesla = ElectricCar("Tesla", "Model S", 100)
print(tesla.show_info())
