i=0
num=int(input("How many rows u want to print = "))
ascii_value=65
while i<num:
    j=0
    while j<=i:
        print(chr(ascii_value+j),end="")
        j+=1
    print()
    i+=1