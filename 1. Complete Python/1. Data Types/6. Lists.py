# Creating a list
clothes = ["Tshirt", "Shirt", "Jeans"]
# Adding item trousers to list
clothes.append("Trousers")
print(f"Clothes are: {clothes}")
# Removing item
clothes.remove("Trousers")
print(f"Clothes are: {clothes}")

# Extending list
wardrobe = ["watches", "shoes"]
wardrobe.extend(clothes)
print(f"Items in wardrobe are: {wardrobe}")

# Adding items using index number
wardrobe.insert(2, "socks")
print(f"Updated items in wardrobe are: {wardrobe}")

# Popping last element and storing it in a variable
last_item = wardrobe.pop()
print(f"Item popped: {last_item}")
print(f"New Wardrobe: {wardrobe}")

# Reversing list
wardrobe.reverse()
print(f"Reversed wardrobe: {wardrobe}")

# Sorting list by alphabets
wardrobe.sort()
print(f"Sorted wardrobe: {wardrobe}")

# Max and min
wardrobe_storage = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"Maximum wardrobe size: {max(wardrobe_storage)}")
print(f"Minimum wardrobe size: {min(wardrobe_storage)}")

# Adding lists by '+' [Operator Overloading]
accessories = ["Silver metal watch", "Ajmal Silver shade"]
new_wardrobe = clothes + accessories
print(f"New wardrobe items are: {new_wardrobe}")