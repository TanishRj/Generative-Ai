# Getting seat type
seat_type = input("Enter your seat type (sleeper/AC/general/luxury) : ").lower()

# Matching seat type using case
match seat_type:
    case "sleeper":
        print("Sleeper - Nothing beyond beds")
    case "ac":
        print("AC - Air conditioned beds")
    case "general":
        print("General - Cheapest beds")
    case "luxury":
        print("Luxury - Premium beds with meals")
    # If bad input
    case _:
        print("Invalid seat type")