fname=input("Enter the File Name:")
num=int(input("Enter the number of students:"))
#Each line represents a student and starts with 0 (student(0),student(1) etc)
for i in range(num):#optional u can manually create a file instead of inputting 
    with open(fname,'a') as file:
        file.write(input("Enter student[i] details:"))
        file.write("\n")#till here its optional

student_list=[]
with open(fname,'r') as file:
    for line in file:
        student_list.append(line.strip().split(' '))

student_marks=[]

for i in range(num):
    sum=0
    avg=0
    for j in student_list[i]:
        sum=sum+int(j)
        
    print(f"Student[{i}] Sum:{sum}")
    avg=float(sum/6)
    print(f"Student[{i}] Average:{avg}")
    student_marks.append(sum)
    student_marks.append(avg)
    student_marks.append("*")#* represents end of student

print(student_marks)
