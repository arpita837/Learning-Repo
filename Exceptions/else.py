try:
    result = 10 / 5
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    print("Division result:", result)
finally:
    print("This will always be executed.")
