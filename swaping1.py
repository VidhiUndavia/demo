#write a program to swap two numbers
num1=int(input("Enter first number = "))
num2=int(input("Enter second number = "))
print("------------Before swapping--------------")
print("First = ",num1)
print("Second = ",num2)
print("------------After swapping--------------")
# using third variable
# temp=num1
# num1=num2
# num2=temp

# without third variable

num1=num1+num2
num2=num1-num2
num1=num1-num2

print("First = ",num1)
print("Second = ",num2)