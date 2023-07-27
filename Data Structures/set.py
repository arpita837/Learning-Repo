# Creating a set using curly braces
my_set = {1, 2, 3}

# Creating a set using set() function
another_set = set([3, 4, 5])

# Adding elements to the set
my_set.add(4)

# Removing elements from the set
my_set.remove(2)

# Performing set operations (union, intersection, etc.)
union_set = my_set.union(another_set)
intersection_set = my_set.intersection(another_set)

print(my_set)  # Output: {1, 3, 4}
print(union_set)  # Output: {1, 3, 4, 5}
print(intersection_set)  # Output: {3}
