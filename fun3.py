# no argument with return value
def getInterest():
    principle=int(input("Enter the amount = "))
    rate=float(input("Enter the rate = "))
    no_of_years=int(input("Enter the year = "))
    si=principle*rate*no_of_years/100
    return si
interest=getInterest()
print("Interest = ",interest)

# output
# D:\python_3>py fun2.py
# Enter the amount = 10000
# Enter the rate = 5.6
# Enter the year = 3
# Interest =  1680.0 