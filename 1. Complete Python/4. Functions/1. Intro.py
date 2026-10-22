# Example - 1
# Creating function print_order which accepts parameters name and coffee type
def print_order(name, coffee_type):
    print(f"{name} ordered {coffee_type} coffee")

# Calling function
# print_order("Tanish", "Black Coffee")
# print_order("Raj", "Americano")
# print_order("Hitesh", "Cappuccino")

# Example - 2
# Fetching sales function
def fetch_sales():
    print(f"Fetching sales")

# Filtering sales function
def filter_valid_sales():
    print(f"Filtering valid sales data")

# Filtering sales function
def summarize_data():
    print(f"Summarizing sales data")

# Generate report function
def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print(f"Report is Ready")

# Calling main generate report function
generate_report()