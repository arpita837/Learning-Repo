# Creating a list
my_list = [1, 2, "hello", 3.14]

# Accessing elements of the list
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: hello

# Modifying elements of the list
my_list[1] = 10
print(my_list)  # Output: [1, 10, 'hello', 3.14]

# Adding elements to the list
my_list.append(42)
print(my_list)  # Output: [1, 10, 'hello', 3.14, 42]

# Removing elements from the list
my_list.remove('hello')
print(my_list)  # Output: [1, 10, 3.14, 42]
