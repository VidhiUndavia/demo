num=input("Enter the number = ")
length=len(num)
sum=0
print("\n\n------------For Loop------------")
for i in num:
    sum+=int(i)**length
if sum==int(num):
    print("Its an armsttrong number")
else:
    print("Its not an armsttrong number")
i=0
sum=0
print("------------While Loop------------")
while i<length:
    sum+=int(num[i])**length
    i+=1
if sum==int(num):
    print("Its an armsttrong number")
else:
    print("Its not an armsttrong number")