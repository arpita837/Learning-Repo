class MyClass:
    static_variable = value

class Car:
    # Static variable
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_details(self):
        print(f"Make: {self.make}, Model: {self.model}, Wheels: {Car.wheels}")

# Create instances of the Car class
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Display details of both cars
car1.display_details()  # Output: Make: Toyota, Model: Corolla, Wheels: 4
car2.display_details()  # Output: Make: Honda, Model: Civic, Wheels: 4

# Access the static variable directly from the class
print(Car.wheels)  # Output: 4
