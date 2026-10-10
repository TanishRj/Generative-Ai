# Creating main function of order
def placed_order():
    # creating order variable
    original_order = "Pizza"
    # Creating nested function for new order
    def new_order():
        # use the variable from its parent fuction and modify its value
        nonlocal original_order
        # New value of variable from parent function
        original_order = "Pizza + Burger"
    # Calling inner function 
    new_order()
    # Printing updated value
    print("After order update, order is", original_order)

# Calling main function
placed_order()