def reverse(number):
    sum=int(0)
    while number!=0:
        rem=int(number%10)
        sum=int(sum*10+rem)
        number=int(number/10)
    return sum

num=int(input("Enter the number:"))
temp=reverse(num)
if num==temp:
    print("Number is Palindrome:")
else:
    print("Not a palindrome:")

print("The reversed No=",temp)