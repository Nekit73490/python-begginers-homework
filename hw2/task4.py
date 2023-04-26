# 4. Задайте список из N элементов, заполненных числами из 
# промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# 5. Реализуйте алгоритм перемешивания списка.

posd = open('file.txt','r')

positions = []

for line in posd:
    positions.append(line)

real_pos = [int(i.replace('\n', '')) for i in positions]

our_n = int(input())
n_list = []
for i in range(our_n*(-1),our_n+1):
    n_list.append(i)

import random


work_list = n_list

midlist = []

for i in range(len(n_list)):
    rand_n = random.randrange(len(work_list))
    midlist.append(work_list[rand_n])
    del work_list[rand_n]

print(midlist)
print(real_pos)

multi = 1
for i in real_pos:
    multi = multi * midlist[i]


print(multi)