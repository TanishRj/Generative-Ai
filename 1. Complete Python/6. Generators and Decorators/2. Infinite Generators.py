# Unlimited Cars
def unlimited_cars():
    count = 1
    while True:
        yield f"Replacement no #{count}"
        count += 1

cars = unlimited_cars()

for _ in range(5):
    print(next(cars))