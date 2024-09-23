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

# output
# D:\python_3>py nested_loop2.py
# How many rows u want to print = 5
# A
# AB
# ABC
# ABCD
# ABCDE
