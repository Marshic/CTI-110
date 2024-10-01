# This program simulates shopping and displays receipt
print("----YOUR PURCHASE!----")
print()
# Values
shoppername = str(input("Enter your profile name: "))
print()
item1 = input("Enter first item: ")
quantity1 = int(input(f"Enter the quantity of {item1}: "))
price1 = float(input(f"Enter the price of {item1}: "))
print()

item2 = input("Enter second item: ")
quantity2 = int(input(f"Enter the quantity of {item2}: "))
price2 = float(input(f"Enter the price of {item2}: "))
print()

item3 = input("Enter third item: ")
quantity3 = int(input(f"Enter the quantity of {item3}: "))
price3 = float(input(f"Enter the price of {item3}: "))
print()
# Calculate
subtotal = (quantity1 * price1) + (quantity2 * price2) + (quantity3 * price3)
salestax = (subtotal * .07)
total = (subtotal + salestax)

#Together
print(f"Thanks for Shopping at Rainbow Road {shoppername} !")
print("-*-" * 20)
print()
item = "ITEM"
quantity = "QUANTITY"
price = "PRICE"
print(f"{item:<30}{quantity:<15}{price:<20}")
print()
print(f"{item1:<30}{quantity1:<15}${price1 * quantity1:.2f}")
print(f"{item2:<30}{quantity2:<15}${price2 * quantity2:.2f}")
print(f"{item3:<30}{quantity3:<15}${price3 * quantity3:.2f}")
print()
print("-*-" * 20)
#Receipt
print(f"{shoppername}'s receipt!")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${salestax:.2f}")
print()
print(f"Total: ${total:.2f}")

