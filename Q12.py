l1=[]
def indexOfSmallesElement(l1):
    x=min(l1)
    return l1.index(x)

n=int(input())

for i in range(n):
    x=int(input())
    l1.append(int(x))

print("Smallest Index:",indexOfSmallesElement(l1))

