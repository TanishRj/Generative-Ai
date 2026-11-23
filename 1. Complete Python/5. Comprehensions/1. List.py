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
volvo_car = [car for car in cars if "Volvo" in car]

print(volvo_car)