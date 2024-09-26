# Name
# 9/24/2024
# P1LAB1
# Get input from the user and calculate travel expenses

print("----Calculate your travel expenses !----")
print()
print()


# Get input from user
budget = float(input("Enter Budget: "))
travelDes = str(input("Enter your travel destination: "))
fuel = float(input("How much do you think you'll spend on gas? "))
accomodation = float(input("Approximately, how much will you need for accomodation/hotel: "))
food = float(input("Lastly, how much wil you need for food? "))
print()
print()
#Calculate
remainder = budget - (fuel + accomodation + food)

#Display to user
print("----Travel Expenses----")

print("Location:", travelDes)
print("Initial Budget:", budget)
print()

print("Fuel:", fuel)
print("Accomodation:", accomodation)
print("Food:", food)
print()

print("Remainding Balance: ", remainder)

