num=int(input("Enter the number"))

temp=2
flag=0
while temp<num:
    if num%temp==0:
        flag=1
        break
    temp+=1
if flag==1:
    print("Its not a prime number")
else:
    print("Its a prime number")