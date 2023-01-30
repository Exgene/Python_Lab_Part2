strMerge=""
str1=input("Enter string1:")
str2=input("Enter string2:")

for i in str1:
    if i.isupper():
        strMerge+=i

for i in str2:
    if i.isupper():
        strMerge+=i

print(strMerge)