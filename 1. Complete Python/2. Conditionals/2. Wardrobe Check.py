# Getting input from user and converting it into lower case
wardrobe = input("Enter your cloth name: ").lower()
print(f"User entered: {wardrobe}")

# Conditions
if wardrobe == "tshirt" or wardrobe == "shirt":
    print(f"Nice, you can get {wardrobe}")
else:
    print(f"The item {wardrobe} isn't available in wardrobe")