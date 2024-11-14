# Donte' Brown
# 10/29/2024
# P3HW2
# This program calculates paycheck based on OT or no OT
# Declaring variables for results of loop
numEmployees = 0
amountOT = 0
amountRH = 0
amountGross = 0
# Get input from user
name = input("Enter employee's name or 'Done' to terminate: ")

while name.lower() != "done":
    numEmployees += 1
    hours = float(input(f"Enter {name}'s hours worked: "))
    payrate = float(input(f"Enter {name}'s payrate: "))
    if hours > 40:
        OT = hours - 40
        regpay = payrate * 40
        amountRH += regpay
        OTPR = (payrate * 1.5)
        OT_pay = OTPR * OT
        amountOT += OT_pay
        gross = OT_pay + regpay
        amountGross += gross
    else:
        OT = 0
        regpay = payrate * hours
        amountRH += regpay
        OTPR = (payrate * 1.5)
        OT_pay = OTPR * OT
        amountOT += OT_pay
        gross = regpay
        amountGross += gross
    print (f"{'Hours Worked':<15}{'Pay Rate':<15}{'Overtime':<15}{'Overtime Pay':<15}{'Regular Pay':<15}{'Gross Pay':<15}")
    print (f"-" * 60)
    print(f"{hours:<15}{payrate:<15}{OT:<15}${OT_pay:<15.2f}${regpay:<15.2f}${gross:<15.2f}")
    name = input("Enter employee name or 'done' to calculate: ")
print("-"*60)
# Display results to user
print (f"Total number of employees entered: {numEmployees}")
print (f"Total amount paid for overtime: ${amountOT:.2f}")
print (f"Total amount paid for regular hours: ${amountRH:.2f}")
print (f"Total amount paid for gross: ${amountGross:.2f}")
