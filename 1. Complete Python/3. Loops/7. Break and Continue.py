# Creating a flavors list
flavors = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

# Looping through list
for flavor in flavors:
    # Checking if flavor is out of stock, skip that 
    if flavor == "Out of Stock":
        # don't continue the loop to check for discontinued item
        continue
    # Break the loop and come outside
    if flavor == "Discontinued":
        break
    print(f"{flavor} item found")

print(f"Outside the loop")