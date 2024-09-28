def marks(english,maths,science):
    print("Englilsh = ",english,"Maths = ",maths,"Science = ",science)
Maths=int(input("Enter maths marks  = "))
Science=int(input("Enter science marks  = "))
English=int(input("Enter english marks  = "))
marks(English,Maths,Science)
marks(Maths,Science,English)
marks(maths=Maths,science=Science,english=English)
# output
# D:\python_3>py keyword_arg.py
# Enter maths marks  = 70
# Enter science marks  = 67
# Enter english marks  = 75
# Englilsh =  75 Maths =  70 Science =  67
# Englilsh =  70 Maths =  67 Science =  75
# Englilsh =  75 Maths =  70 Science =  67