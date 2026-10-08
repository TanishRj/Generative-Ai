# Example - 1
# Getting user input
def get_input():
    print(f"Getting Input")

# Validating user input
def validate_input():
    print(f"Validating Input")

# Saving to Database
def save_to_db():
    print(f"Saving to Database")

# Registering user
def register_user():
    get_input()
    validate_input()
    save_to_db()
    print(f"User Registration")

# Calling main register function
# register_user()

# Example - 2

# Function that returns the total bill
def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

# Storing the returned value from function
my_bill = calculate_bill(5, 50)
# print(f"Total Bill: {my_bill}")

# Example - 3

# Getting price and vat rate
def add_vat(price, vat_rate):
    # Adding 10% of vat
    return price * (100 + vat_rate)/100

# 3 orders
orders = [100, 150, 200]

# Adding vat for each order and printing prices
for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Original Price : {price}, Final price with VAT: {final_amount}")