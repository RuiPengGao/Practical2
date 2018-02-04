#determine grade

num = float(input("Enter score: "))

if (70<=num<=100):
    print("A")
elif (60<=num<70):
    print("B")
elif (55<=num<60):
    print("C")
elif (50<=num<55):
    print("D")
elif (45<=num<50):
    print("E")
elif (35<=num<45):
    print("S")
elif (0<=num<35):
    print ("U")
else:
    print("number entered is invalid")
