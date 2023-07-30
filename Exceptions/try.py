try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Exception handling code for ZeroDivisionError
    print("Error: Cannot divide by zero!")
finally:
    # Cleanup code in the finally block
    print("This will always be executed.")
