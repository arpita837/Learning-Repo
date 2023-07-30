class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
obj = MyClass("Alice", 30)
obj.display_info()
# Output: Name: Alice, Age: 30
