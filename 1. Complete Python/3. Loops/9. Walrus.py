# Walrus operator allows you to assign values to expression

# Example - 1
# Assigning a value
value = 13

# Checking the remainder by creating and storing the variable in remainder
if remainder := value % 5:
    print(f"Not Divisible, remainder is {remainder}")

# Example - 2

# Creating a list of cars
available_cars = ["bmw", "audi", "mercedes"]

# Creating and checking the car is prensent in list using walrus operator
if (requested_car := input("Enter your car name : ")) in available_cars:
    print(f"Serving")