# Inr Prices
phone_prices_inr = {
    "Samsung A27": 27000,
    "Iphone 16": 80000,
    "Motorola": 20000,
}

# Converting into usd
# Gets phone name and price from dictionary
# + get both key and value pair using items()
# + Return both key and value using :
# + Evaluate both using (/ 90) expression 
phone_usd_prices = {phone_name:price / 90 for phone_name, price in phone_prices_inr.items()}
print(phone_usd_prices)