#validating triangles and computing perimeters

num1 = float(input("Enter side_1: "))
num2 = float(input("Enter side_2: "))
num3 = float(input("Enter side_3: "))

if ((num1 + num2) > num3 and (num2 + num3) > num1 and (num1 + num3) > num2):
    print("Valid triangle!")
    perimeter = num1 + num2 + num3
    print ("perimeter of triangle is: {:.2f}".format(perimeter))

else:
    print("Invalid triangle!")
    
