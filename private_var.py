class bank:
    def __init__(self,name,acctype,balance):
        self.name=name
        self.acctype=acctype
        self.__balance=balance
acc=bank("pooja","current",1000)
acc.name="janu"
acc.__balance=500000
print(acc.__balance)
    