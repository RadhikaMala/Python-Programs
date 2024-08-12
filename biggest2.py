a=int(input("Enter num1:"))
b=int(input("Enter num2:"))
c=int(input("Enter num3:"))
if a>b and a>c:
    print("{} is greater".format(a))
elif b>a and b>c:
    print("{} is greater".format(b))
else:
    print("{} is greater".format(c))
