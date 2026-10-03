# Smart discount system
order_status = input("Enter your order status: ").lower()

# Checking if order is placed successfully or not
if order_status == "placed successfully":
    # Checking value of order
    order_value = int(input("Enter your order value : "))
    # Discount applicable only above 1000
    if order_value > 1000:
        print(f"You have got 20% discount code as DISC20")
    else:
        print(f"Order is not eligible for discount") 
# If order was not placed
else:
    print(f"Order not placed") 