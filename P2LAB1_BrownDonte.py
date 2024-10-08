# Donte' Brown
# 10/8/24
# P2LAB1
# Using Python's built-in library

import math

# Ask for radius from user
radius = float(input("What is the radius of the circle?: "))
pi = math.pi
print()
# Calculations

diameter = radius * 2
circum = radius * 2 * pi
area = pi * radius ** 2

# Display results to user

print(f"The diameter of the circle is {diameter:.1f}\n")
print(f"The circumference of the circle is {circum:.2f}\n")
print(f"The area of the circle is {area:.3f}\n")
