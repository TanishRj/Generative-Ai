customer_name = "Tanish"
customer_item = "Shoes"

print(f"Items are {customer_item} for customer {customer_name}")

# INDEXING
item_description = "Black Nike Shoes without laces"
# Getting first word
print(f"First word: {item_description[0:6]}")
# Getting every second character
print(f"Word after every 2nd char: {item_description[0:6:2]}")
# Getting last word
print(f"Last word: {item_description[10:]}")
# Reversing string 
print(f"Reversed String: {item_description[::-1]}")

# Encoding special characters
enc_string = "Encoded shoés"
encoded_label = enc_string.encode("utf-8")
decoded_label = encoded_label.decode("utf-8")
print(f"Encoded Label: {encoded_label}")
print(f"Decoded Label: {decoded_label}")