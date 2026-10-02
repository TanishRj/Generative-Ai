# Cafe Menu

user_food = input("Choose your food (burger/pizza/pasta): ").lower()

if user_food == "burger":
    print(f"{user_food} Price is 250 Rs")
elif user_food == "pizza":
    print(f" {user_food} Price is 400 Rs")
elif user_food == "pasta":
    print(f"{user_food} Price is 300 Rs")
else:
    print(f"{user_food} isn't available now ")