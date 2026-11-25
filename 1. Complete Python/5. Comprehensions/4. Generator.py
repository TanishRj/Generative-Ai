# Daily Customers
daily_customers = [2,4,5,4,7,8,5]

# Sum all the customers using generators
total_customers = sum(customer for customer in daily_customers if customer > 1)
print(total_customers)