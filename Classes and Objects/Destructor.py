class MyClass:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print(f"Object {self.name} is being destroyed.")
obj1 = MyClass("Object1")
obj2 = MyClass("Object2")
# Output: Object Object1 is being destroyed.
#         Object Object2 is being destroyed.
