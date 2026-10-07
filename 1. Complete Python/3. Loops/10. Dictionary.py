# Creating users dictionary
users = [
    {"id": 1, "total":100, "coupon":"P20"},
    {"id": 2, "total":150, "coupon":"F10"},
    {"id": 3, "total":80, "coupon":"P50"}
]

# Creating discounts dictionary
dicounts = {
    "P20": (0.2, 0),
    "F10": (0.5, 0),
    "P50": (0.2, 0)
}

# Creating discounts for users
for user in users:
    percent, fixed = dicounts.get(user["coupon"], (0,0))