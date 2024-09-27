def nsquare(x=2,y=1):
    ans=x*x+2*x*y+y*y
    return ans

result=nsquare(4,2)
print("Answer = ",result)
result=nsquare(3)
print("Answer = ",result)
result=nsquare()
print("Answer = ",result)