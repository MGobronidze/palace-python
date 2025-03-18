class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    def greet(self):
        super().greet()  # მშობლის greet() მეთოდის გამოძახება
        print("Hello from Child!")

c = Child()
c.greet()
