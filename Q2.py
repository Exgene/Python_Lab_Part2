eno=int(input("Enter Employeee ID : "))
ename=str(input("Enter Employee Name : "))
ebasic=int(input("Enter the Basic Salary : "))
eallow=int(input("Enter the Employee Allowance :"))

gross=eallow+ebasic

if gross<=5000:
    IT=0
elif (gross>=5001 and gross<=10000):
    IT=gross*0.1
elif (gross>=10001 and gross<=20000):
    IT=gross*0.2
elif gross>=20001:
    IT=gross*0.3

netpay=gross-IT

print("Basic Salary : ",ebasic)
print("Allowances : ",eallow)
print("Gross Pay : ",gross)
print("Income Tax : ",IT)
print("Net Pay : ",netpay)