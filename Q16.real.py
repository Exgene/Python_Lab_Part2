class Account:
    def __init__(self,accNo,bal=100):
        self.__accNo=accNo
        self.__bal=bal
    
    def deposit(self,amount):
        self.__bal+=amount
    
    def withdraw(self,amount):
        if self.__bal<=amount+100:
            print("No Money")
        else:
            self.__bal-=amount
    
    def display(self):
        print("Account NO:",self.__accNo)
        print("Balance:",self.__bal)
    
    def getAcc(self):
        return self.__accNo
    
    def getBal(self):
        return self.__bal

l1=[]

def NewAcc(accNo):
    for i in l1:
        if i.getAcc()==accNo:
            print("Number Already Present")
            return
    l1.append(Account(accNo))
    print(l1)

n=int(input("Number of New Acc:"))
for i in range(n):
    x=int(input("Enter the Number"))
    NewAcc(x) 

def MaxAcc():
    maxBal=0
    maxAcc=None
    for i in l1:
        if i.getBal()>maxBal:
            maxBal=i.getBal()
            maxAcc=i
    print("MaxBal:",maxBal)
    print("MaxAccNo:",maxAcc.getAcc())

def process(acc,op,amt):
    for i in l1:
        if i.getAcc()==acc:
            if op==1:
                i.deposit(amt)
                return
            elif op==2:
                i.withdraw(amt)
                return
            elif op==3:
                i.display()
                return                   
                       
while(1):
    print("1.Deposit\n2.Withdraw\n3.Display\n4.Max\n5.Exit")
    print("Enter the Choice:")   
    x=int(input())
    if x==1:
        x=int(input("AccNumber:"))
        amt=float(input("Enter the amount to be Deposited:"))
        process(x,1,amt)
    elif x==2:
        x=int(input("AccNumber:"))
        amt=float(input("Enter the amount to be Withdrawn:"))
        process(x,2,amt)
    elif x==3:
        x=int(input("AccNumber:"))
        process(x,3,0)
    elif x==4:
        MaxAcc()
    elif x==5:
        exit(0)
    else:
        print("Invalid")
    



        