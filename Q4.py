mark_list = {'John' : 86.5, 'Jack' : 91.2, 'Jill' : 84.5, 'Harry': 72.1, 'Joe': 80.5}
sorted_keys = sorted(mark_list, key=mark_list.get, reverse=True)
print("top 3 students")
for student in sorted_keys[:3]:
    print(student, ": ", mark_list[student])
sum = 0
for student in mark_list:
     sum += mark_list[student]
print("average marks :", sum/len(mark_list))