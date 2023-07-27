def greet_person(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Calling the function without providing the 'greeting' parameter
greet_person("Alice")  # Output: Hello, Alice!

# Calling the function with a custom greeting
greet_person("Bob", greeting="Hi")  # Output: Hi, Bob!
