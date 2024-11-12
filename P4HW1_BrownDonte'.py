# Donte' Brown
# 11/12/24

# Get number of scores
numScores = int(input("How many scores do you want to enter: "))

validgrades = []

for grade in range(numScores):
    thisGrade = input(f"Enter score #{grade + 1}: ")
    #Loop to ensure thisItem is in availableItems
    while thisGrade < 0 or thisGrade > 100:
        print(f"{thisGrade} is invaid")
        thisGrade = input(f"Enter score #{grade + 1} again: ")

# Loop to print each score
validgrades.append(thisGrade)
#Calculate

lowest = min(validgrades)
highest = max(validgrades)
sum_num = sum(validgrades)
avg = sum(validgrades)/len(validgrades)

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
validgrades.remove(lowest)
print(f"{'Modified List:':<25} {validgrades:.1f}")
print(f"{'Average:':<25} {avg:.2f}")
print("-" * 31)
print()
