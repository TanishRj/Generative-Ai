# Name list
names = ["Tanish", "Aditya", "Ravi", "Naman"]
# Bill list
bill = [500, 1000, 100, 350]

# Merging 2 lists using zip that returns values from each list
for idx, bl in zip(names, bill):
    print(f"{idx} has to pay: {bl} amount")