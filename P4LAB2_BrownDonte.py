# Donte' Brown
# 11/7/24
# P4LAB2
# Use loops to show only positive times tables
run_again = "yes"

while run_again.lower() != "no":
    number = int(input("Enter an integer: "))
    
    if number >= 0:
        for i in range(1, 13):
            print(f"{number} * {i} = {number * i}")
    else:
        print("This program doesn't accept negative numbers.")

    run_again = input("Would you like to run the program again? (yes/no): ").strip().lower()
print("Program has ended...")
