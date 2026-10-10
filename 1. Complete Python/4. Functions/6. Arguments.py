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
names_list(names)