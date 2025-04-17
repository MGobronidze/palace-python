# polymorphism in Built-in Functions
print(len("Hello"))  # String length
print(len([1, 2, 3]))  # List length

print(max(1, 3, 2))  # Maximum of integers
print(max("a", "z", "m"))  # Maximum in strings


# polymorphism in functions
def add(a, b):
    return a + b

print(add(3, 4))           # Integer addition
print(add("Hello, ", "World!"))  # String concatenation
print(add([1, 2], [3, 4])) # List concatenation

# polymorphism in oop
class Shape:
    def area(self):
        return "Undefined"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Rectangle(2, 3), Circle(5)]
for shape in shapes:
    print(f"Area: {shape.area()}")



# types of polymorphism
class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())  # Calls the overridden method based on the object type


# Inheritance Class Polymorphism
class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
    
# ways of implementing polymorphism
# duck typing
class GFGCoder:
	def execute(self):
		print("Geeks are working on the code...")

class Geeks:
	def code(self, executor):
		executor.execute()

# Create instances of the classes
executor = GFGCoder()
ide = Geeks()

# Call the code method using the IDE instance
ide.code(executor)
 
#  Method overloading
class GFG:
	def sum(self, a = None, b = None, c = None):		 
		s = 0
		if a != None and b != None and c != None:
			s = a + b + c
		elif a != None and b != None:
			s = a + b
		else:
			s = a
		return s
	
s = GFG()
# sum of 1 integer
print(s.sum(1))
# sum of 2 integers
print(s.sum(3, 5))
# sum of 3 integers
print(s.sum(1, 2, 3))


# # error
# # class Student:
# class Student:
# 	def __init__(self, m1, m2):
# 		self.m1 = m1
# 		self.m2 = m2

# S1 = Student (58, 60)
# S2 = Student (60, 58)

# # this will generate an error
# S3 = S1 + S2

# solution 
class Student:

	# defining init method for class
	def __init__(self, m1, m2):
		self.m1 = m1
		self.m2 = m2

	# overloading the + operator
	def __add__(self, other):
		m1 = self.m1 + other.m1
		m2 = self.m2 + other.m2
		s3 = Student(m1, m2)
		return s3

s1 = Student(58, 59)
s2 = Student(60, 65)
s3 = s1 + s2
print(s3.m1)

# method overriding 
# parent class
class Programming:
	# properties
	DataStructures = True
	Algorithms = True
	# function practice
	def practice(self):
		print("Practice makes a man perfect")
	# function consistency
	def consistency(self):
		print("print from programming")
		
# child class	 
class Python(Programming):
	# function 
	def consistency(self):
		print("Hard work along with consistency can defeat Talent.")

Py = Python()
Py.consistency()
Py.practice()
