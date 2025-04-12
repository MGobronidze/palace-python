class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # მშობელი კლასის კონსტრუქტორის გამოძახება
        self.breed = breed

    def speak(self):
        return "Bark"

dog = Dog("Buddy", "Labrador")
print(dog.name)  # Buddy
print(dog.breed) # Labrador
print(dog.speak())  # Bark
