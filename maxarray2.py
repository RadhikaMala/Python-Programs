a=list(map(int,input("Enter num:").split(",")))
max_num=a[0]
for n in a[1:]:
    if n>max_num:
        max_num=n
print(max_num)
