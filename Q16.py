class Account:
    def __init__(self,number):
        self.__accNum=number
        self.__balance=100
    
    def withdraw(self,amt):
        if self.__balance<100:
            print("Insufficient Balance!")
        else:
            self.__balance=self.__balance-amt
    
    def deposit(self,amt):
        self.__balance+=amt
    
    def getAccNumber(self):
        return self.__accNum
    
    def getBalance(self):
        return self.__balance

list=[]
    
def NewAccount(accNo):
    for i in list:
        if i.getAccNumber()==accNo:
            print("Number Already Present!")
        else:
            list.append(Account(accNo))

def Process(num , op , amt):
    for i in list:
        if i.getAccNumber()==op:
            if op=="deposit":
                i.deposit(amt)
            elif op=="withdraw":
                i.withdraw(amt)
            elif op=="balance":
                print("Balance:",i.getBalance())
        return
    print("Acc Number Not Found!")

def MaxAccBal(num):
    maxBal=0
    maxAcc=None
    for i in list:
        if i.getBalance()>maxBal:
            maxBal=i.getBalance
            maxAcc=i
    print(f"Max Balance of the Acc No :{maxAcc.getAccNumber()} is {maxBal}")

def main():
    n=int(input("Enter the Number of accs(0 to skip):"))
    for i in range(n):
        f=int(input("Enter a valid Acc Number:"))
        NewAccount(f)
    while(1):
        accNo=int(input("Enter Your Account Number:"))
        print("1.DEPOSIT\n2.WITHDRAW\n3.BALANCE\n4.MAXACC\n5.EXIT")
        x=int(input("ENTER A CHOICE"))
        if x==1:
            amt=float(input("Enter the amount"))
            Process(accNo,"deposit",amt)        
        elif x==2:
            amt=float(input("Enter the amount"))
            Process(accNo,"withdraw",amt)
        elif x==3:
            Process(accNo,"balance",0)
        elif x==4:
            MaxAccBal(accNo)
        elif x==5:
            exit()
        else:
            print("Invalid Input!")

main()


        