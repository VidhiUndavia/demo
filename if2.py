idproof=int(input("If u have id proof then enter 1 otherwise 0 = "))
citizen=int(input("If u are indian then enter 1 or 0 = "))
age=int(input("Enter your age = "))

if age>=18 and idproof==1 and citizen==1:
    print("You can do votting")
else:
    print("You are not eligible for votting")
print("Good bye")
