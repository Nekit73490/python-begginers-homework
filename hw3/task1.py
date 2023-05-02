work_list = [2,3,5,9,3]

our_multi = 0

for indexx, value in enumerate(work_list):
    if indexx % 2:    
        print('Элемент', work_list[indexx],'был на нечётной позиции')
        our_multi = our_multi + value

print('\n')
print('Сумма элементов на нечётных позициях =', our_multi)