first=int(input("Enter the first number = "))
second=int(input("Enter second number = "))

print("-----------Menu------------")
print("1 = Addition")
print("2 = Subtraction")
print("3 = Multiplication")
print("4 = Division")
choice=int(input("Enter yoour choice   u want to perform the operation"))
if choice==1:
    print("Addition = ",first+second)
elif choice==2:
    print("Substraction = ",first-second)
elif choice==3:
    print("Multiplication = ",first*second)
elif choice==4:
    print("Division = ",first/second)
# else:
#     print("Invalid input")
# print("Finish")