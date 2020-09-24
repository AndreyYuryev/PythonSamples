year = int(input())
leap_year = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
if leap_year:
    print("Yes")
else:
    print("No")
