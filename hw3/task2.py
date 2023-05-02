working_list = input('enter your list of numbers, separated by commas ')

working_list = [int(i) for i in working_list.split(',')]

our_length = len(working_list) #just for clarity/readability of code

print('your pairs are: ')

for i in range(our_length//2):
    print(working_list[i] * working_list[-i-1])

if our_length%2 :
    print((working_list[our_length//2])**2)
