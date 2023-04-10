num = float(input())
num = str(num)
num = num.replace('.','')
num = num.replace('-','')
num_sum = 0
for i in num:
    num_sum = num_sum + int(i)
print(num_sum)