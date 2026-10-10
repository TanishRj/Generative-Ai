def placed_order():
    original_order = "Pizza"
    def new_order():
        nonlocal original_order
        original_order = "Pizza + Burger"
    new_order()
    print("After order update, order is", original_order)

placed_order()