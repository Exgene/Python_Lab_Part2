mark_list={"John":86.5,"Jack":91.2,"Jill":84.5,"Harry":72.1,"Joe":80.5}
sorted_list=sorted(mark_list,key=mark_list.get,reverse=True)
print("Top 3 students:")
for i in sorted_list[:3]:
    print(i+" with marks:",mark_list[i])

sum=0
for i in sorted_list:
    sum+=mark_list[i]

print("Avg:",sum/len(mark_list))