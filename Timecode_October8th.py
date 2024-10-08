# Using Python built-in libraries
# Import the datetime library to use it in the program

import datetime

# Assign the current date and time to a variable
time = datetime.datetime.now()
month = time.month

month_word = time.strftime("%B")


# Display date/time
print(f"The current date and time is {time}")
print(f"The current month is {month}")
print(f"The current month is {month_word}")

today = datetime.datetime.today()
print(f"Today is {today}")

weekday = today. weekday()
weekday = int(weekday)
print(type(weekday))
print(f"The day of the week is {weekday}\n")

# Gets the data type of the variables
print(type(weekday))
weekday = int(input("Enter a value 0-6: "))

#if-else statements to determine the day of the week
if weekday == 0:
    weekday_word = "Monday"

elif weekday == 1:
    weekday_word = "Tuesday"

elif weekday == 2:
    weekday_word = "Wednesday"

elif weekday == 3:
    weekday_word = "Thursday"

elif weekday == 4:
    weekday_word = "Friday"

elif weekday == 5:
    weekday_word = "Saturday"
    
elif weekday == 6:
    weekday_word = "Sunday"
else:
        print (f"INVALID DAY OF THE WEEK!!!")
        weekday_word = "Invalid"

print()
print (f"The day of the week is {weekday_word}")
