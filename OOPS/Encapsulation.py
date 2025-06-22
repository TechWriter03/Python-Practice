class Account:

    def __init__(self,accNo):
        # private variables 
        self.__accNo=accNo
        self.__bal=0

    def credit(self,amount):
        self.__bal+=amount
        print("Rs.",amount,"was credited")
        print("Available Balance:",self.getBalance())
        print()

    def debit(self,amount):
        if self.__bal<amount:
            print("Insufficient Balance")
            print()
        else:
            self.__bal-=amount
            print("Rs.",amount,"was debited")
        print("Available Balance:",self.getBalance())
        print()

    def getAccNo(self):
        return self.__accNo

    def getBalance(self):
        return self.__bal
    
acc1=Account(123)
acc1.credit(1000)
acc1.debit(300)
acc1.debit(800)

print("Account Number:",acc1.getAccNo())
print("Available Balance:",acc1.getBalance())
