# storing yield in variable
def car_order():
    print("Welcome, what car you want")
    order = yield
    while True:
        print(f"Booking: {order}")
        # If any order comes up after previous one
        order = yield

car = car_order()
next(car) # Start Generator

# Sends value to yield
car.send("BMW")
car.send("Audi")
