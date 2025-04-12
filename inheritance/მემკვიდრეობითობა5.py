class Bird:
    def fly(self):
        return "Bird is flying with wings"

class Plane:
    def fly(self):
        return "Plane is flying with engines"

class FlyingCar(Bird, Plane):
    def fly(self):
        return f"FlyingCar: {super().fly()}"

flying_car = FlyingCar()
print(flying_car.fly())
