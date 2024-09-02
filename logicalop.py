age=18
citizenship=0
idproof=0
print(age>=18 and  idproof==1 and citizenship==1)
print(not(age>=18 and  idproof==1 and citizenship==1))
print((age>=18 and citizenship==1) or idproof==1)
print(age>=18 and (citizenship==1 or idproof==1))
print(age>=18 and (not(citizenship==1 or idproof==1)))
