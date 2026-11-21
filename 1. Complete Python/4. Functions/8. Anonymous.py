# Recursive Function
def counter(c):
    print("Counter Value: ", c)
    if c == 0:
        return "Counter Reached to 0"
    # Calling function from function
    return counter(c-1)

# print(counter(5))


# Filtration
car_types = ["BMW", "Audi", "BMW", "Mercedes", "Volvo", "Mercedes"]

new_cars = list(filter(lambda car: car=="BMW", car_types))

# Reverse Filtration
old_cars = list(filter(lambda car: car!="BMW", car_types))


print(new_cars)
print(old_cars)