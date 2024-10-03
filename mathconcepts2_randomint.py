# Donte' Brown
# October 3rd
# Pythagorean Calculator CTI-110-5H01

# Import random library for use in the program
import random 

'''
# Get input for the values of the sides from the user.
side1 = float(input("Enter value for side one: "))
side2 = float(input("Enter value for side two: "))
print ("-*-" * 20)
'''

# Generate random values for side1 and side2
side1 = int(random.randint(1, 100))
side2 = int(random.randint(1, 100))

# Values
hypotenuse = (side1 ** 2) + (side2 ** 2)


# Display to user
print (f"A hypotenuse of a right triangle with the sides {side1} and {side2} is equal to {hypotenuse}")
