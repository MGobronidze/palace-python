class Vehicle:
    def __init__(self, brand, model, top_speed):
        self.brand = brand
        self.model = model
        self.top_speed = top_speed

    def drive(self):
        return f"{self.brand} {self.model} is driving at {self.top_speed} km/h"

    def __str__(self):
        return f"{self.brand} {self.model} (Top speed: {self.top_speed} km/h)"

    def __repr__(self):
        return f"Vehicle({self.brand!r}, {self.model!r}, {self.top_speed!r})"

    def __eq__(self, other):
        return (
            isinstance(other, Vehicle)
            and self.brand == other.brand
            and self.model == other.model
        )

    def __lt__(self, other):
        return self.top_speed < other.top_speed

class Car(Vehicle):
    def __init__(self, brand, model, top_speed, num_doors):
        super().__init__(brand, model, top_speed)
        self.num_doors = num_doors

    def drive(self):
        return f"{self.brand} {self.model} drives smoothly with {self.num_doors} doors."

class Motorcycle(Vehicle):
    def drive(self):
        return f"{self.brand} {self.model} speeds off on two wheels!"

class Truck(Vehicle):
    def __init__(self, brand, model, top_speed, max_load):
        super().__init__(brand, model, top_speed)
        self.max_load = max_load

    def drive(self):
        return f"{self.brand} {self.model} is carrying {self.max_load} tons!"

def __add__(self, other):
    if isinstance(other, Vehicle):
        return Vehicle(
            brand=f"{self.brand}-{other.brand}",
            model=f"{self.model}-{other.model}",
            top_speed=(self.top_speed + other.top_speed) // 2
        )
    raise TypeError("You can only add another Vehicle")
Vehicle.__add__ = __add__

def race(vehicles):
    for v in vehicles:
        print(v.drive())

c1 = Car("Toyota", "Corolla", 180, 4)
m1 = Motorcycle("Yamaha", "R1", 299)
t1 = Truck("Volvo", "FH16", 120, 20)

vehicles = [c1, m1, t1]

race(vehicles)

combo = c1 + m1
print(combo)

# student task
# Add __len__() to return number of wheels.
# Add a method get_type() in each subclass and use duck typing.
# Add a feature to sort vehicles by speed using sorted().
# Add a Bus subclass with passenger capacity.
# Let students override __str__ with more info in subclasses.
# Simulate a vehicle garage with a class Garage that can store and manage vehicles.