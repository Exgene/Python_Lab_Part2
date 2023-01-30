l1=[]
def BinarySerach(key):
    low=int(0)
    high=int(len(l1))

    while(low<=high):
        mid=int((low+high)/2)
        if(int(l1[mid])==key):
            return mid
        elif(int(l1[mid])<key):
            low=mid+1
        else:
            high=mid-1
    
    return -1

n=int(input("How many Numbers?"))
for i in range(n):
    x=int(input(f"Enter Number[{i+1}]"))
    l1.append(x)
key=int(input('Enter the search element:'))

l1=sorted(l1)
print(l1)

x=BinarySerach(key)

if(x>=0):
    print("FOund in Location:",x)
else:
    print("Not found")