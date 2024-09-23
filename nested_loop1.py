# *
# * *
# * * *
# * * * *

num=int(input("How many rows u want to print = "))
i=0
while i<num:
    j=4
    temp=1
    while j>=i:
        print(temp,end="")
        temp+=1
        j-=1
    print()
    i+=1
