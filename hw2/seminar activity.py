# colors = ['green','blue','orange']
# data = open('secondfile.txt','a')
# data.writelines(colors)
# data.close()



# 1. Напишите программу, которая принимает на вход число N и выдаёт
# последовательность из N членов, подчиняющихся закону f(i) = 3^i*(-1)^i,
# где i - индекс элемента последовательности.
# Пример:
# - Для N = 5: 1, -3, 9, -27, 81

# num = int(input('enter desired number '))

# ans_list = list(range(num))

# for i in range(num):
#     ans_list[i] = (3**i)*((-1)**i)

# print(ans_list)

#__________________________

# 2. Для натурального n создать словарь индекс-значение, состоящий из
#  элементов последовательности 3n + 1.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


# num = int(input('enter desired number '))

# ans_dic = {i+1 : (i+1)*3+1 for i in range(num)}

# print(ans_dic)



# 3. Напишите программу, в которой пользователь будет задавать две
#  строки, а программа - определять количество вхождений одной строки в другой.

text1 = input('Введите первую строку: ')
text2 = input('Введите вторую строку: ')
counter = 0
if len(text1) > len(text2): # сравниваем длины строк
    for i in range(len(text1)):
        if text1[i:i + len(text2)] == text2: # проверяем, равна ли посдтрока в строке по длинне среза, второй строки
            counter += 1
else:
    for i in range(len(text2)):
        if text2[i:i + len(text1)] == text1:
            counter += 1
print('Колличество вхождений второй строки в первую равно: ', counter)