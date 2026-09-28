# BOOLEANS
is_living = True # Counts as 1
total_men = 5
total_living_things = total_men + is_living # Upcasting
print(f"Total Living Things: {total_living_things}") 

# Conversion
men_present = 1 # Man present = True
women_present = 0 # Women present = False
print(f"Is men present? {bool(men_present)}") 
print(f"Is women present? {bool(women_present)}") 

# OPERATORS
is_paper_present = True
is_pen_present = False
is_pencil_present = True

can_write = is_paper_present and is_pen_present or is_pencil_present
print(f"Can we write: {can_write}")

# Float
current_temp = 50.51
max_temp = 50.60
print(f"Current Temperature {current_temp}")
print(f"Maximum Temperature {max_temp}")
print(f"Difference in Temperature {max_temp - current_temp}")
