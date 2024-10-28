# I was supposed to put a comment here
# Donte' Brown
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 4: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))

# Add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum_grad = sum(grades)
avg = sum(grades)/len(grades)

# Determine letter grade for averageif avg >= 90:
if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
else:
    grade = 'F'
# Display to user
print("------------Results------------")

print(f"{'Lowest Grade:':<25} {low:.1f}")
print(f"{'Highest Grade:':<25} {high:.1f}")
print(f"{'Sum of Grades:':<25} {sum_grad:.1f}")
print(f"{'Average:':<25} {avg:.2f}")
print("-" * 31)
print(f'Your grade is: {grade}')
print()

