n=int(input("Enter number:"))
fact=1
for i in range(2,n+1):
    fact=fact*i
print("factorial of {} is {}".format(n,fact))
