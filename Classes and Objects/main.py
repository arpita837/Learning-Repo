class Dog:
    species = "Canine"
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    def bark(self):
        return "Woof!"
    def get_description(self):
        return f"{self.name} is a {self.species} and is {self.age} years old."
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
print(dog1.name)  # Output: Buddy
print(dog2.age)   # Output: 5
print(dog1.species)  # Output: Canine
print(dog2.species)  # Output: Canine
print(dog1.bark())  # Output: Woof!
print(dog2.get_description())  # Output: Max is a Canine and is 5 years old.
