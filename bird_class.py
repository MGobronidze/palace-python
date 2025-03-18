class Bird:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def describe(self):
        return f"{self.name} is {self.color}"

class Parrot(Bird):
    def __init__(self, name, color, can_talk):
        super().__init__(name, color)
        self.can_talk = can_talk
        
parrot = Parrot("Koko","green", True)
print(parrot.describe())


