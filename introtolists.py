# In class examples
# 10/17/2024
# Donte' Brown
# Making a list

# Create an empty list
myfam = []

# Add values to list
myfam.append("Ness")
myfam.append("Joker")
myfam.append("Sora")
myfam.append("Cloud")
myfam.append("Mario")
'''
# Display list
print(myfam)

# Print item at index 3
print(myfam[3])

# Print items from index 1 to 3 (up to but not including 3)
# Add one to your ending
print(myfam[1:4])

# Remove item from list by its value
myfam.remove("Mario")

print(myfam)

# Remove item from list by its index
myfam.pop(3)

print(f"\n\n Remove Sora...")
print(myfam)
'''
num1 = int(input("give number: "))
num2 = int(input("give number: "))
num3 = int(input("give number: "))
num4 = int(input("give number: "))

# Create the list with values in it
numbers = [num1, num2, num3, num4]

print(numbers)

# Functions use list

# Give back the number of items in the list
print(f"There are {len(numbers)} items in the list.")

# Get the highest value in the list
print(f"The highest value in the list is {max(numbers)}.")

# Get the lowest value in the list
print(f"The lowest value in the list is {min(numbers)}.")

# Get the average
average = sum(numbers)/len(numbers)

# Display average
print(f"The average of the values in the list is {average}.")
