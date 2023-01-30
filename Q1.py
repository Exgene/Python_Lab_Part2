ENAME=input("ENter employee name")
EID=int(input("ENter ID"))
hrs=int(input("Hrs worked per week"))
rate=float(input("Pay rate per hr"))

def mpay(hrs,rate):
    Mpay=hrs*rate*4
    return Mpay

PAY=mpay(hrs,rate)
print("MOnthly pay:",PAY)