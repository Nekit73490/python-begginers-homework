N = int(input('input target number '))
multi = 1
N_list = []

for i in range(N):
    multi = multi * (i+1)
    N_list.append(multi)
print(N_list)