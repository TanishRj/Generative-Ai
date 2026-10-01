# Sets
essential_things = {"Phone", "Laptop", "Charger"}
optional_things = {"Wallet", "Laptop"}

# Union (All)
all_things = essential_things | optional_things
print(f"All things: {all_things}")

# Intersection
common_things = essential_things & optional_things
print(f"Common things: {common_things}")

# Only essential
only_essential = essential_things - optional_things
print(f"Only present in essential: {only_essential}")

# Check items in sets