global_var = "I'm global!"

def outer_function():
    # Enclosing scope
    outer_var = "I'm in the outer function!"
    
    def inner_function():
        # Local scope
        local_var = "I'm in the inner function!"
        print(local_var)
        print(outer_var)
        print(global_var)

    inner_function()

outer_function()
