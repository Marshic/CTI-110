# Donte' Brown
# 11/14/24
# P4HW2
# Example similar to P4HW using loops

'''
While
    Get product until user types "exit" to terminate
    user to enter cost of product
        Increase # of products
        Increase total cost
# loop breaks
display total # products
total cost
'''
# Create variables to hold totals
numItems = 0
totalcost = 0
# Get input from user/variables
product = input("Enter product name or 'exit' to terminate: ")

while product.lower() != "exit":
    numItems += 1
    cost = float(input(f"Enter cost of {product}: "))
    totalcost += cost 
    print()
    product = input("Enter product name or 'exit' to terminate: ")
print (f"-" * 60)

print (f"Number of items: {numItems}")
print (f"Total: ${totalcost:.2f}")
