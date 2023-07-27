original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extracting [2, 3, 4]
slice3 = original_list[1:4]

# Extracting [5, 6, 7, 8, 9]
slice4 = original_list[4:]

print(slice3)  # Output: [2, 3, 4]
print(slice4)  # Output: [5, 6, 7, 8, 9]

original_tuple = (10, 20, 30, 40, 50)
# Extracting (20, 30, 40)
slice5 = original_tuple[1:4]

# Extracting (30, 40, 50)
slice6 = original_tuple[2:]

print(slice5)  # Output: (20, 30, 40)
print(slice6)  # Output: (30, 40, 50)
