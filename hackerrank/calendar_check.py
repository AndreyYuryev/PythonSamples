import calendar

month, day, year = input().split(' ')
calendar.TextCalendar(firstweekday=0)
weekday = calendar.weekday(day=int(day), month=int(month), year=int(year))
if 2000 < int(year) < 3000:
    print(calendar.day_name[weekday].upper())