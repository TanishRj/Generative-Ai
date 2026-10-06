# Creating a flavours list
flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

# Looping through list
for flavour in flavours:
    # Checking if flavour is out of stock, skip that 
    if flavour == "Out of Stock":
        # don't continue the loop to check for discontinued item
        continue
    # Break the loop and come outside
    if flavour == "Discountinued":
        break
