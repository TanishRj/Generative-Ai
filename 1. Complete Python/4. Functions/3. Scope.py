# Local scope variable
def day_name():
    day = "Sunday"
    print(f"Inside Function: {day}")

# Global Scope
day = "Monday"
day_name()
print(f"Outside Function : {day}")

# Enclosing Scope