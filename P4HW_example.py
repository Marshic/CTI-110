# Donte' Brown
# 11/12/24
# P4HW1 example
'''
Ask user how many grades
    Loop to run however many times they requested
        check to mke sure grade between zero and 100
            If score is valid, add to list
                invalid scores not accepted
'''
# Create list
availableitems = ["spiderdonut", "toyknife", "monstercandy", "mandana", "snailpie", "snowmanpiece", "nicecream", "dogsalad"]

# Get number of items to purchase
numItems = int(input("How many items will you purchase?: "))

# Empty list to hold valid responses
cart = []
# Loop to get new items
for item in range(numItems):
    thisItem = input(f"Enter item #{item + 1}: ")
    #Loop to ensure thisItem is in availableItems
    while thisItem not in availableitems:
        print(f"{thisItem} is NOT for sale GOOFY try again")
        thisItem = input(f"Enter item #{item + 1} again and get it right: ")
    # Add the valid item to the cart
    cart.append(thisItem)

# Loop to print each item in cart
print()
print("Item(s) purchased")
for product in cart:
    print(product)