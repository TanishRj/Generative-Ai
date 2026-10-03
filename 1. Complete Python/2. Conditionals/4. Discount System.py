# Smart discount system
order_status = input("Enter your order status: ").lower()

if order_status == "placed successfully":
    order_value = int(input("Enter your order value : "))
    if order_value > 1000:
        print(f"You have got 20% discount code as DISC20")
    else:
        print(f"Order is not eligible for discount") 
else:
    print(f"Order not placed") 