class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self._age = None  # Private attribute
        self._grade = None  # Private attribute
        self.age = age  # Using setter
        self.grade = grade  # Using setter

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0 or value > 100:
            raise ValueError("Age must be between 0 and 100.")
        self._age = value

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if value < 0.0 or value > 100.0:
            raise ValueError("Grade must be between 0 and 100.")
        self._grade = value

    def display_info(self):
        return f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}%"


# Creating student objects
try:
    student1 = Student("Alice", 20, 85.5)
    student2 = Student("Bob", 17, 92.0)
    print(student1.display_info())
    print(student2.display_info())

    # Trying invalid data
    student3 = Student("Charlie", -5, 75)  # This will raise an error
except ValueError as e:
    print(f"Error: {e}")
