# Donte' Brown
# 10/10/24
# P2LAB2
# Using Dictionaries

# Create a Dictionary
cars = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}

# Variable that hold only keys from dictionary
keys = cars.keys()

# Show all the keys to the user
print(keys)
print()
# Get input from user
selected_car = input("Enter a vehicle to see it's MPG: ")

# Display selected car and its miles per gallon
print (f"The {selected_car} gets {cars[selected_car]} mpg.")

# Ask user how many miles they'll drive
miles_planned = float(input(f"How many miles will you drive the {selected_car}?: "))

# Calculations
total_gas = miles_planned / cars[selected_car]

# Display
print (f"{total_gas:.2f} gallon(s) of gas are needed to drive the Prius {miles_planned} miles.")


                      
