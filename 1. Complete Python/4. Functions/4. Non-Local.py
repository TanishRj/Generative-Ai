def placed_order():
    original_order = "Pizza"
    def new_order():
        nonlocal original_order
        original_order = "Pizza + Burger"
        