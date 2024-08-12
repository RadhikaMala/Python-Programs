n=int(input("Enter number:"))
for i in range(1,n+1):
    isprime = True
    for j in range(2,i):
        if i%j == 0:
            isprime = False
if isprime:
    print("It is a prime number")
else:
    print("It is not a prime number")
