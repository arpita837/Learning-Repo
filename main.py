# Example of Update
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict1.update(dict2)
print(dict1)

# Example of Comparison
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 1, 'b': 2}

print(dict1 == dict2)

dict3 = {'a': 1, 'b': 2, 'c': 3}

print(dict1 != dict3)

# Example of Length
my_dict = {'a': 1, 'b': 2, 'c': 3}

print(len(my_dict))
# Example of Copy
original_dict = {'a': 1, 'b': 2}
copied_dict = original_dict.copy()

copied_dict['c'] = 3
print(original_dict)
print(copied_dict)

# Example of Items
my_dict = {'a': 1, 'b': 2, 'c': 3}

print(my_dict.items())

# Example of String Representation
my_dict = {'a': 1, 'b': 2, 'c': 3}

print(str(my_dict))



