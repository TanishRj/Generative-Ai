# Creating new order
original_order = "Pizza"

# Creating main function
def new_order():
    # Creating nested function
    def menu():
        # Accessing varible from the whole code
        global original_order
        # Modifying the variable value
        original_order = "Pizza + Burger"
    # Calling inner function
    menu()
    print("New order is : ", original_order)

# Calling main function
new_order()