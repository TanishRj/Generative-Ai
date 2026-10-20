# Local scope variable
def day_name():
    day = "Sunday"
    print(f"Inside Function: {day}")

# Global Scope
day = "Monday"
day_name()
print(f"Outside Function : {day}")

# Enclosing Scope
def month_name():
    month = "October"

    def print_month():
        month = "November"
        print(f"Inner Month : {month}")
    print_month()    
    print(f"Outer Month : {month}")

month_name()