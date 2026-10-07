# Creating a list of users
users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80, "coupon": "P50"}
]

# Creating a dictionary of discount rules
# Each coupon stores: (percentage_discount, fixed_discount)
discounts = {
    "P20": (0.2, 0),   # 20% discount
    "F10": (0.5, 0),   # 50% discount
    "P50": (0, 10)     # ₹10 fixed discount
}

# Loop through each user
for user in users:

    # Get the coupon used by the user
    # If the coupon doesn't exist, use (0, 0)
    percent, fixed = discounts.get(user["coupon"], (0, 0))

    # Calculate the total discount
    discount = user["total"] * percent + fixed

    # Display the user's payment and discount
    print(
        f"{user['id']} paid {user['total']} "
        f"and got discount for next visit of rupees {discount}"
    )