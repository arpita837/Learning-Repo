# Creating a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'}

# Accessing values using keys
print(my_dict['name'])  # Output: Alice
print(my_dict['age'])   # Output: 30

# Modifying values using keys
my_dict['age'] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'email': 'alice@example.com'}

# Adding new key-value pairs to the dictionary
my_dict['city'] = 'New York'
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'email': 'alice@example.com', 'city': 'New York'}

# Removing key-value pairs from the dictionary
del my_dict['email']
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}
