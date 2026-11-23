# Creating lists of cars to filter
cars = [
    "BMW M4",
    "Volvo XC90",
    "Audi R8",
    "Mercedes Benz GLA"
]

# Gets expression (value) 
# + search for all cars in lists 
# + Checks volvo string in expression
volvo_car = [vol_car for vol_car in cars if "Volvo" in vol_car]

print(volvo_car)