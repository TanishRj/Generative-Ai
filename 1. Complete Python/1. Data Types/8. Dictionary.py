# Dictionary
person1_details = dict(name="Tanish", gender="Male", Age=21)
print(f"Person Details: {person1_details}")

# Adding key:value 
person2_details = {}
person2_details["Name"] = "Tanish New"
person2_details["Age"] = 21
print(f"Person 2 Name: {person2_details['Name']}")

# Removing value
del person2_details["Age"]
print(f"Person 2 without age: {person2_details}")

# Checking value
print(f"Does age exists in person 1: {'Age' in person1_details}")

# Checking keys, values and items
person3_details = dict(name="Ramesh", gender="Male", Age=25)
# Keys
# print(f"Person 3 (keys): {person3_details.keys()}")
# Values
# print(f"Person 3 (values): {person3_details.values()}")
# Items
# print(f"Person 3 (items): {person3_details.items()}")

# Removing last item
last_item = person3_details.popitem()
print(f"Removed last item: {last_item}")

# Update details
add_details = {"Work" : "Developer", "Mode" : "Remote"}
person3_details.update(add_details)

print(f"New Person 3 Details: {person3_details}")

# Get specific values
# Exists
# person3_work = person3_details["Work"]
# print(f"Person 3 Work: {person3_work}")
# Not Exists
# not_exists = person3_details["extra activities"]
# print(f"Person 3 non existing: {not_exists}")

# Getting specific values using get
person3_work = person3_details["Work"]
print(f"Person 3 Work: {person3_work}")
not_exists = person3_details.get("Extra activities", "Didn't get extra activities")
print(f"Person 3 non existing: {not_exists}")
  