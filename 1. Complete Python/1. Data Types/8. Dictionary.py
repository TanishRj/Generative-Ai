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

# Checking keys and values
person3_details = dict(name="Ramesh", gender="Male", Age=25)
# Keys
print(f"Person 3 details: ")