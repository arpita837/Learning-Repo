import numpy as np
# 1D array
arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d)

# 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)

# Initializing arrays with zeros and ones
zeros_arr = np.zeros((3, 4))
ones_arr = np.ones((2, 3))
print(zeros_arr)
print(ones_arr)

# Creating a range of values
range_arr = np.arange(0, 10, 2)
print(range_arr)

# Creating a random array
random_arr = np.random.rand(3, 3)
print(random_arr)
# Element-wise arithmetic operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

add_result = a + b
sub_result = a - b
mul_result = a * b
div_result = a / b
print(add_result, sub_result, mul_result, div_result)

# Dot product
dot_product = np.dot(a, b)
print(dot_product)

# Transpose of an array
arr = np.array([[1, 2, 3], [4, 5, 6]])
transpose_arr = arr.T
print(transpose_arr)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Slicing
slice1 = arr[2:6]
slice2 = arr[:5]
slice3 = arr[6:]
print(slice1, slice2, slice3)

# Indexing
value = arr[3]
print(value)

# 2D array slicing and indexing
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
slice_row = arr_2d[1]
slice_column = arr_2d[:, 2]
print(slice_row, slice_column)
