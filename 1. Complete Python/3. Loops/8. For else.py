# Creating staff list
staff = [("Tanish", 17), ("Raj", 15), ("Hitesh", 16)]

# Creating a for else loop
for name, age in staff:
    if age <= 18:
        # breaks at the first true iteration i.e breaks after Tanish
        print(f"{name} is eligible to manage the staff")
        break
else:
    print(f"No one is eligible to manage staff")