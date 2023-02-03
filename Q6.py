str=input("Enter the string:")
a={'a':0,'e':0,'i':0,'o':0,'u':0}

for i in str:
    if i in a:
        a[i]+=1

print(a)

