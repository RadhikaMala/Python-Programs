num=int(input("Enter number:"))
reserved_num=0
while num>0:
    digit=num%10
    reserved_num=reserved_num*10+digit
    num=num//10
print(reserved_num)
