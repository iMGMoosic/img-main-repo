month = int(input("Please enter the month: "))
day = int(input("Please enter the day: "))
year = int(input("Please enter the year: "))

if month <= 2:
    month += 12
    year -= 1

day_of_week = (day + 5 + (26 * (month + 1) // 10) + (5 * (year % 100) // 4) + (21 * (year // 100) // 4)) % 7

if day_of_week == 0:
    day_of_week = "Monday"
elif day_of_week == 1:
    day_of_week = "Tuesday"
elif day_of_week == 2:
    day_of_week = "Wednesday"
elif day_of_week == 3:
    day_of_week = "Thursday"
elif day_of_week == 4:
    day_of_week = "Friday"
elif day_of_week == 5:
    day_of_week = "Saturday"
else:
    day_of_week = "Sunday"

if month > 12 and month <= 14:
    month -= 12
    year += 1

print(str(month)+"/"+str(day)+"/"+str(year)+" is on a "+str(day_of_week))
