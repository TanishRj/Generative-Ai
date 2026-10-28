# Example - 1 (Printing Parameter)
# Variable to store value as "Tanish"
name = "Tanish"

# Creating new function that prints person's name
def print_name(person):
    print("The person's name is: ", person)

# Calling function
# print_name(name)

# Example - 2 (Editing Lists)
# Creating names list
names = ["Tanish", "Raj", "Aditya"]

# Function that changes name at 1st index and prints it
def names_list(new_list):
    new_list[1] = "Aryan"
    print("New names list is: ", new_list)

# Calling main function
# names_list(names)

# Example - 3 (Positional and Keyword Arguments)

# Defining functions that prints details
def details(name, age, gender):
    print(name, age, gender)

# Positional Arguments
# details("Tanish", 21, "Male")
# Keyword Based Arguments
# details(name="Tanisha", gender="Female", age=19)

# Example - 4 (args and *Kwargs)
# Function which takes args ad kwargs as parameters
# (*name) = take everything without any key
#  (**age) = Take everything with keys
def new_details(*name, **age):
    print("Names are: ", name)
    print("Ages are: ", age)

# Printing names and age
# new_details("Tanish", "Raju", "Shubham", age_tanish=21, age_raju=22, shubham_age=24)

# Example - 5 (Appending only when value provided)
# Defining a function which takes the name only when provided
def new_names_list(names=None):
    # If name is not there, the array is empty
    if names is None:
        names = []    
    print(names)
# Calling main function
new_names_list()    