# 2.CALENDER 
import calendar

# Sunday se week start karne ke liye setfirstweekday ka use karein
calendar.setfirstweekday(calendar.SUNDAY)

year = int(input("Enter year: "))
month = int(input("Enter month: "))

cal = calendar.monthcalendar(year, month)

# Ab header ko bhi Sunday se start kar dein
print("Su Mo Tu We Th Fr Sa")
for week in cal:
    for day in week:
        if day == 0:
            print("  ", end=" ")
        else:
            print(f"{day:2}", end=" ")
    print()