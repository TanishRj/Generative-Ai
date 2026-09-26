# IMMMUTABLE
amount = 12
# print(f"Initial Amount : {amount}")

amount = 24
# print(f"New Initial Amount : {amount}")


# Immutable because they are changing reference of amount variable in memory from 2 to 12
# Printing ID of both 12 and 24 for checking reference change
# print(f"Id of 2: {id(12)}")
# print(f"Id of 12: {id(24)}")

# MUTABLE using set function from python
jug = set()
print(f"Initial jug id : {id(jug)}")
# Adding values using add
jug.add("Water")
jug.add("Salt")
jug.add("Lemon")

# Printing Values
print(f"Initial jug id : {jug}")

# Printing formatted id after adding values
print(f"Initial jug id : {id(jug)}")
