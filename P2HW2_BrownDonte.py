# Donte
# 10/17/24
# P2HW2
# Get input from the user and calculate module grades

print("----Calculate Module Grades !----")
print()
print()


# Get input from user
Module1 = float(input("Enter grade for Module 1: "))
Module2 = float(input("Enter grade for Module 2: "))
Module3 = float(input("Enter grade for Module 3: "))
Module4 = float(input("Enter grade for Module 4: "))
Module5 = float(input("Enter grade for Module 5: "))
Module6 = float(input("Enter grade for Module 6: "))
print()
print()

# Create list for calculations
modules = [Module1, Module2, Module3, Module4, Module5, Module6]

#Calculate
lowest = min(modules)
highest = max(modules)
sum_num = sum(modules)
average = sum(modules)/len(modules)

#Display to user
print("------------Results------------")

print(f"{'Lowest Grade:':<25} {lowest:.1f}")
print(f"{'Highest Grade:':<25} {highest:.1f}")
print(f"{'Sum of Grades:':<25} {sum_num:.1f}")
print(f"{'Average:':<25} {average:.2f}")
print("-" * 31)
print()


