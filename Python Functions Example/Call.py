def greet():
    print("Hello, world!")

# Call the greet() function
greet()  # Output: Hello, world!


def add_numbers(a, b):
    sum_result = a + b
    print("Sum:", sum_result)

# Call the add_numbers() function with arguments
add_numbers(5, 3)  # Output: Sum: 8


def calculate_sum_and_product(a, b):
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result

# Call the calculate_sum_and_product() function and use the return values
result_sum, result_product = calculate_sum_and_product(5, 3)
print("Sum:", result_sum)       # Output: Sum: 8
print("Product:", result_product)  # Output: Product: 15


# Using built-in functions
result = len("Hello")  # Call the len() function to get the length of the string
print("Length:", result)  # Output: Length: 5

result = max(3, 7, 1, 9)  # Call the max() function to get the maximum value
print("Maximum:", result)  # Output: Maximum: 9
