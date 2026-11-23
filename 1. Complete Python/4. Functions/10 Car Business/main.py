# METHOD 1 - Importing whole file
# Importing bmw file under cars
import cars.bmw

# Importing methods from bmw file
print(cars.bmw.bmw_m3())
print(cars.bmw.bmw_m4())

# METHOD 2 - Importing methods directly
from cars.bmw import bmw_m3, bmw_m4

print(bmw_m3())
print(bmw_m4())

