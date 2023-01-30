index=0
count=0
word=input("Enter a word")
for i in word:
    if i.isupper():
        print("Letter:"+ i)
        print("Index:",index)
        count+=1
    index+=1
print("Count=",count)

    
