# მშობელი კლასი (Animal)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "ზოგადი ცხოველის ხმა"

# შვილობილი კლასი (Dog)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "ძაღლი")
        self.breed = breed

    def make_sound(self):
        return "ვაუფ ვაუფ!"  # ძაღლის სპეციფიკური ხმა

# ობიექტის შექმნა
dog1 = Dog("ბობი", "ლაბრადორი")

print(dog1.name)         # ბობი
print(dog1.species)      # ძაღლი
print(dog1.breed)        # ლაბრადორი
print(dog1.make_sound()) # ვაუფ ვაუფ!
