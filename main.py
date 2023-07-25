try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Exception handling code for ZeroDivisionError
    print("Division by zero is not allowed.")
finally:
    # Clean-up code (always executed)
    print("Cleaning up resources.")
try:
    file = open("data.txt", "r")
    # Code to read data from the file
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    # Clean-up: Close the file (always executed)
    file.close()
# Example of Garbage Collection
def create_large_list():
    # This function creates a large list, but once the function finishes, the list will be garbage collected.
    large_list = [i for i in range(1000000)]
    # 'large_list' will be automatically garbage collected once the function returns.

create_large_list()  # Call the function to create the list.

# Example of explicit deletion using 'del'
my_list = [1, 2, 3]
del my_list
# The 'my_list' object has been deleted explicitly and will be garbage collected.
