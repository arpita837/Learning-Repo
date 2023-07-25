def get_user_info():
    name = "John Doe"
    age = 30
    email = "john.doe@example.com"
    return name, age, email

# Call the function and receive the multiple return values
user_name, user_age, user_email = get_user_info()

print(f"Name: {user_name}")
print(f"Age: {user_age}")
print(f"Email: {user_email}")
