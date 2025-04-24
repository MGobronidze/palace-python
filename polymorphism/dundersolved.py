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
        return isinstance(other, Vehicle) and self.brand == other.brand and self.model == other.model

    def __lt__(self, other):
        return self.top_speed < other.top_speed

    def __add__(self, other):
        if isinstance(other, Vehicle):
            return Vehicle(
                brand=f"{self.brand}-{other.brand}",
                model=f"{self.model}-{other.model}",
                top_speed=(self.top_speed + other.top_speed) // 2
            )
        raise TypeError("You can only add another Vehicle")


class Car(Vehicle):
    def __init__(self, brand, model, top_speed, num_doors):
        super().__init__(brand, model, top_speed)
        self.num_doors = num_doors

    def drive(self):
        return f"{self.brand} {self.model} drives smoothly with {self.num_doors} doors."

    def __len__(self):
        return 4

    def get_type(self):
        return "Car"

    def __str__(self):
        return f"{self.brand} {self.model} - {self.num_doors} doors (Top speed: {self.top_speed} km/h)"


class Motorcycle(Vehicle):
    def drive(self):
        return f"{self.brand} {self.model} speeds off on two wheels!"

    def __len__(self):
        return 2

    def get_type(self):
        return "Motorcycle"

    def __str__(self):
        return f"{self.brand} {self.model} (Motorcycle, Top speed: {self.top_speed} km/h)"


class Truck(Vehicle):
    def __init__(self, brand, model, top_speed, max_load):
        super().__init__(brand, model, top_speed)
        self.max_load = max_load

    def drive(self):
        return f"{self.brand} {self.model} is carrying {self.max_load} tons!"

    def __len__(self):
        return 6

    def get_type(self):
        return "Truck"

    def __str__(self):
        return f"{self.brand} {self.model} (Truck - Max Load: {self.max_load} tons, Top speed: {self.top_speed} km/h)"


class Bus(Vehicle):
    def __init__(self, brand, model, top_speed, passenger_capacity):
        super().__init__(brand, model, top_speed)
        self.passenger_capacity = passenger_capacity

    def drive(self):
        return f"{self.brand} {self.model} carries {self.passenger_capacity} passengers."

    def __len__(self):
        return 6

    def get_type(self):
        return "Bus"

    def __str__(self):
        return f"{self.brand} {self.model} (Bus - {self.passenger_capacity} passengers, Top speed: {self.top_speed} km/h)"


class Garage:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        if isinstance(vehicle, Vehicle):
            self.vehicles.append(vehicle)

    def __str__(self):
        return f"Garage has {len(self.vehicles)} vehicles:\n" + "\n".join(str(v) for v in self.vehicles)

    def __len__(self):
        return len(self.vehicles)

    def __contains__(self, vehicle):
        return vehicle in self.vehicles


def race(vehicles):
    for v in vehicles:
        print(v.drive())


# Sample usage
def main():
    c1 = Car("Toyota", "Corolla", 180, 4)
    m1 = Motorcycle("Yamaha", "R1", 299)
    t1 = Truck("Volvo", "FH16", 120, 20)
    b1 = Bus("Mercedes", "Sprinter", 140, 20)

    vehicles = [c1, m1, t1, b1]
    race(vehicles)

    print("\n-- Vehicle Types --")
    for v in vehicles:
        print(f"{v.get_type()}: {v}")

    print("\n-- Sorted by Top Speed --")
    for v in sorted(vehicles):
        print(v)

    print("\n-- Vehicle Combination --")
    combo = c1 + m1
    print(combo)

    print("\n-- Garage --")
    garage = Garage()
    garage.add_vehicle(c1)
    garage.add_vehicle(t1)
    garage.add_vehicle(b1)
    print(garage)
    print("Is Corolla in garage?", c1 in garage)
    print("Garage size:", len(garage))


if __name__ == "__main__":
    main()
