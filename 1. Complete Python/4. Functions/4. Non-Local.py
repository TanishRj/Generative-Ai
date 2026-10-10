# Creating main function of order
def placed_order():
    # creating order variable
    original_order = "Pizza"
    # Creating nested function for new order
    def new_order():
        nonlocal original_order
        original_order = "Pizza + Burger"
    new_order()
    print("After order update, order is", original_order)

placed_order()