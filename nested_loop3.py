row=5
i=0

while i<row:
    space=row
    while space>i:
        print("   ",end="")
        space=space-1
    j=0
    while j<=i:
        print(" * ",end="")
        j+=1
    print()
    i+=1

