l1=[]
n=int(input("Enter the Number:"))

for i in range(n):
    x=int(input("Enter all the numbers"))
    l1.append(int(x))

for i in range(n):
    for j in range(n-1):
        if l1[i]>l1[j]:
            l1[i],l1[j]=l1[j],l1[i]

print(l1)




