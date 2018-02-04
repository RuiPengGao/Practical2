#detemine leap year

Year = int(input("Enter year here:"))

if (Year % 400) ==0:
    print("{0} is a leap year".format(Year))
elif (Year % 100) ==0:
    print("{0} is not a leap year".format(Year))
elif (Year % 4) == 0:
    print("{0} is a leap year".format(Year))
else:
    print("{0} is not a leap year".format(Year))
