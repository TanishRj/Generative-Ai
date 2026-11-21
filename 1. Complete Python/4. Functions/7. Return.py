# With Return
def car_stock():
    # Returning value of car stock as 20
    return 20

return_car_stock = car_stock()
print(return_car_stock)

# Without returning anything
def no_car_stock():
    pass

return_no_car_stock = no_car_stock()
print(return_no_car_stock)

# Early return (nothing after return)
def new_car_stock():
    return 30
    # Not printed
    print("New car stock launched")

return_new_stock = new_car_stock()
print(return_new_stock)

# Multiple values
def cars():
    return "BMW", "Audi", "Mercedes"

car1, car2, car3 = cars()
print(car1)
print(car2)
print(car3)