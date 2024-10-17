# Donte
# 10/8/24
# P2HW1
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
print("------------Travel Expenses------------")

print(f"{'Location:':<25} {travelDes}")
print(f"{'Initial Budget:':<25} ${budget:,.2f}")
print(f"{'Fuel:':<25} ${fuel:,.2f}")
print(f"{'Accomodation:':<25} ${accomodation:,.2f}")
print(f"{'Food:':<25} ${food:,.2f}")
print("-" * 39)
print()

print(f"{'Remainding Balance:':<25} ${remainder:,.2f}")

