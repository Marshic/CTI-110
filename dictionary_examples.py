# Donte' Brown
# 10/10/24
# Dictionaries
# In class example on dictionaries

# Create a dictionary
dragon_arum = {"arum_color":"purple", "arum_price":32.98, "arummax_height":36, "is_perennial":True}
corpse_flower = {"corpse_color":"red", "corpse_price":340.98, "corpsemax_height":11, "is_perennial":False}
# Get value, given the key
print(f"Dragon Arum: ${dragon_arum['arum_price']:.2f}")
print(f"Is the dragon_arum a perennial? {dragon_arum['is_perennial']}")
print(f"Dragon Arum:{dragon_arum['arum_color']}")
print()
print(f"Corpse Flower: ${corpse_flower['corpse_price']:.2f}")
print(f"Is the corpse flower a perennial? {corpse_flower['is_perennial']}")
print(f"Corpse Flower:{corpse_flower['corpse_color']}")
print()

# Add a key value pair
dragon_arum["water_needed"] = "4 oz per day"

# Print the whole dictionary
print(dragon_arum)
print(corpse_flower)

# Add a key value pair
dragon_arum.update({"arumleaf_color":"green", "arumsun_needed":8})
print("\n\n")
corpse_flower.update({"corpseleaf_color":"green", "corpsesun_needed":4})
print("\n\n")
# Print entire dictionary
print(dragon_arum)
print(corpse_flower)
print()
# Remove item from dictionary
del dragon_arum['arummax_height']
print("\n\n")
del corpse_flower['corpsemax_height']

# Print entire dictionary
print(dragon_arum)
print(corpse_flower)
print()

# Print all keys in dictionary
print(dragon_arum.keys())
print(corpse_flower.keys())
# Ask user to give a key in the dictionary
arum_answer = input("Enter a key from a the dragon arum dictionary: ")
corpse_answer = input("Enter a key from a corpse flower dictionary: ")
# Give the value associated with the user's answer
print(f"The value for dragon arum {answer} is {dragon_arum[arum_answer]}")
print(f"The value for corpse flower {answer} is {corpse_flower[corpse_answer]}")

      
