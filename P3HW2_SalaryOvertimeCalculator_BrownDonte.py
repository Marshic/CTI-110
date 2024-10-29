# Donte' Brown
# 10/29/2024
# P3HW2
# This program calculates paycheck based on OT or no OT

'''
Input: Get employee name from user - string (employee)
Input: Get hours worked from user - int (hours)
Input: Get employee payrate from user - float (payrate)

Display: print (f"-"*30)
Display: Employee name

If hours is greater than 40 (employee has OT)
    total hours worked is the variable hours (optional)
    (don't have to create payrate, it already exists)
    Create a variable (OT) that holds only the OT hours (hours - 40)
    Create a variable for overtime payrate (payrate * 1.5)
    Calculate pay for OT hours (OT * OTPR)
    Calculate regular pay (payrate * 40)
    Calculate grosspay (pay for OT + regular pay)
else (No OT - hours has to be 40 or less)
    Create a variable (OT) that holds only the OT hours WHICH IS ZERO!
    Calculate pay for OT hours which is zero
    Calculate regular pay (payrate * hours)
    Calculate grosspay (same as regular pay)
    
Display the line of strings with width specifiers
print(f"{'Hours Worked':<20}{'Pay Rate':<20}")
print(f"{hours:<20}${pay_rate:<20.2f}")
'''
# Get input from user
name = input("Enter employee's name: ")
hours = float(input(f"Enter {name}'s hours worked: "))
payrate = float(input(f"Enter {name}'s payrate: "))
print (f"-" * 60)

# Calculations


if hours > 40:
    OT = hours - 40
    regpay = payrate * 40
    OTPR = (payrate * 1.5)
    OT_pay = OTPR * OT
    gross = OT_pay + regpay
else:
    OT = 0
    regpay = payrate * hours
    OTPR = (payrate * 1.5)
    OT_pay = OTPR * OT
    gross = regpay

# Display results to user

print (f"{'Hours Worked':<15}{'Pay Rate':<15}{'Overtime':<15}{'Overtime Pay':<15}{'Regular Pay':<15}{'Gross Pay':<15}")
print (f"-" * 60)
print(f"{hours:<15}{payrate:<15}{OT:<15}${OT_pay:<15.2f}${regpay:<15.2f}${gross:<15.2f}")




