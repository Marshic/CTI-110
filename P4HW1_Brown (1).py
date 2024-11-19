# Donte' Brown
# 11/12/24
# P4HW1
# Get number of scores
numScores = int(input("How many scores do you want to enter: "))

validgrades = []

for grade in range(numScores):
    thisGrade = int(input(f"Enter score #{grade + 1}: "))
    while thisGrade < 0 or thisGrade > 100:
        print(f"{thisGrade} is invalid. Please enter a valid score between 0 and 100.")
        thisGrade = int(input(f"Enter score #{grade + 1} again: "))
    
    validgrades.append(thisGrade)

#Calculate
lowest = min(validgrades)
validgrades.remove(lowest)  
avg = sum(validgrades) / len(validgrades)  


# Decide the letter grade
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

print(f"{'Lowest score:':<25} {lowest:.1f}")
print(f"{'Modified List:':<25} {validgrades}")
print(f"{'Average:':<25} {avg:.2f}")
print(f"{'Letter Grade:':<25} {grade}")
print("-" * 31)
