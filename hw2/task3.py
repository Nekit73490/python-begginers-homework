cn = int(input())

work_list = []
multi = 0
for i in range(cn):
    work_list.append(round((1+ 1/(i+1))**(i+1),3))
    multi = multi + work_list[i]

print(f"our list is - {work_list} \nit's total sum is - {multi}")