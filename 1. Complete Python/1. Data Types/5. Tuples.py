# Creating tuple
cars = ("bmw", "mercedes", "audi")
# Adding variables to car
(car1, car2, car3) = cars
# Printing cars
print(f"Cars are: {car1}, {car2} and {car3}")

# Another method to create tuple and assign variable
bmw_car, audi_car = 1, 2
print(f"We have {bmw_car} BMW car and {audi_car} Audi car")
# Switching tuple values 
bmw_car, audi_car = audi_car, bmw_car
print(f"We have {bmw_car} BMW car and {audi_car} Audi car")

# Checking if values are present in tuples
print(f"Is toyota present in cars list: {'toyota' in cars} ")
print(f"Is BMW present in cars list: {'bmw' in cars} ")