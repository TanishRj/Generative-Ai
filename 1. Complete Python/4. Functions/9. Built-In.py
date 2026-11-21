# Documenting functions
def new_function(name="Tanish"):
    """This functions returns the name of user"""
    return name

print(new_function.__doc__)
print(new_function.__name__)