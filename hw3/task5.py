
our_size = int(input('Enter the desired size of Fibonacci sequence in one direction - ')) -1

our_list = [0,1]
Negafibonacci_list =[0,1,0]
for i in range(our_size):
    our_list.append(our_list[i+1] + our_list[i])
    Negafibonacci_list.insert(1, Negafibonacci_list[-i-1] - Negafibonacci_list[-i-2])

del Negafibonacci_list[0]
del Negafibonacci_list[-1]

our_list = Negafibonacci_list + our_list
print(our_list)