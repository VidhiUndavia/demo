def getSquare(number):
    square=number*number
    return square
def getcube(number):
    square=getSquare(number)
    ans=square*number
    return ans
num=int(input("Enter the number = "))
ans=getSquare(num,)
print("Square = ",ans)
cube=getcube(num)
print("Cube = ",cube)
