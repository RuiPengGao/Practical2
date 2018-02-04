#number of days in a month in a year


def _leap_year(a,b):
    if (yearValue % 400 ==0):
        return 1 #leap
    elif (yearValue % 100) ==0:
        return 2 #non-leap
    elif (yearValue % 4) == 0:
        return 3#leap
    else:
        return 4#non-leap

monthName = ["Nothing", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
monthLength = ["0", "31", "28", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"]
lmonthLength = ["0", "31", "29", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"]

monthValue = int(input("Month: "))
yearValue = int(input("Year: "))

if _leap_year== (1 and 3):
    user = monthName[monthValue]
    enter = lmonthLength[monthValue]
    print("{}, {} has {}days".format(user, yearValue, enter))
else:
    user = monthName[monthValue]
    enter = monthLength[monthValue]
    print("{},{} has {}days".format(user, yearValue, enter))
