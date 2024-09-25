# with argument no return value
def getInterest(p,r,n):
    si=p*r*n/100
    print("Interest = ",si)
principle=int(input("Enter the amount = "))
rate=float(input("Enter the rate = "))
no_of_years=int(input("Enter the year = "))
getInterest(principle,rate,no_of_years)
# output
# D:\python_3>py fun2.py
# Enter the amount = 10000
# Enter the rate = 5.6
# Enter the year = 3
# Interest =  1680.0 