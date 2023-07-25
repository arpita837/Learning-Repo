def function_name(param1, param2=default_value2, param3=default_value3, ):
    def greet(name, greeting="Hello"):
        print(f"{greeting}, {name}!")

    # Calling the function with only the required parameter
    greet("Alice")  # Output: Hello, Alice!

    # Calling the function with both required and optional parameters
    greet("Bob", "Hi")  # Output: Hi, Bob!

    # Calling the function without providing the optional parameter (uses default value)
    greet("Charlie")  # Output: Hello, Charlie!

