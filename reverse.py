num=int(input("Enter the number = "))
print("Number = ",num)

rev=0
while num>0:
    reminder=num%10
    num=num//10
    rev=(rev*10)+reminder
print("Reverse = ",rev)