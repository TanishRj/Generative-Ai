# Functions with yield
def new_cars():
    yield "Car 1: BMW M3"
    yield "Car 2: VOLVO XC90"
    yield "Car 3: AUDI R8"

# Loop through and print values using next
cars = new_cars()
print(next(cars))
print(next(cars))
print(next(cars))