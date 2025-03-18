class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0  # საწყისი სიჩქარე 0

    def accelerate(self, increase):
        self.speed += increase
        return f"{self.brand} {self.model} ახლა მოძრაობს {self.speed} კმ/სთ სიჩქარით."

    def brake(self, decrease):
        self.speed -= decrease
        if self.speed < 0:
            self.speed = 0
        return f"{self.brand} {self.model} ახლა მოძრაობს {self.speed} კმ/სთ სიჩქარით."

# ობიექტის შექმნა
car1 = Car("Toyota", "Corolla", 2022)

print(car1.accelerate(30))  # Toyota Corolla ახლა მოძრაობს 30 კმ/სთ სიჩქარით.
print(car1.brake(30))       # Toyota Corolla ახლა მოძრაობს 20 კმ/სთ სიჩქარით.
