import math

a=int(input("Coefficient of x^2 : "))
b=int(input("Coefficient of x : "))
c=int(input("Constant : "))

if a*b*c==0:
    print("No Roots !")
    exit(0)


d=(b*b)-(4*a*c)
d=int(d)

if d==0:
    print("Equal and Real Roots")
    x1=x2=-b/(2*a)
    print("Roots are : ",x1,x2)

elif d>0:
    print("Real and Distinct Roots")
    x1=(-b + math.sqrt(d))/(2*a)
    x2=(-b - math.sqrt(d))/(2*a)
    print("Roots are : ",x1,x2)

elif d<0:
    print("Imaginary Roots")
    x1=-b/(2*a)
    x2=math.sqrt(math.fabs(d))/(2*a)
    print(f"Roots are  : {x1}+i{x2} and {x1}-i{x2}")