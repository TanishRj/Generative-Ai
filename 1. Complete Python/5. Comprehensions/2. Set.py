# Complex Example
bikes = {
    "Bajaj": ["Dominar 250", "Domiar 400", "Pulsar"], 
    "Kawasaki": ["Ninja h2r", "z900"],
    "Honda": ["Cb350", "Shine"]
}

# Get all values of keys in dictionary + get each value from values + return each value 
uniuqe_bikes = {model for bike in bikes.values() for model in bike}
print(uniuqe_bikes)