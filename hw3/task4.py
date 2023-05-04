
our_number = int(input())
result_number = ''

while our_number > 0:
    result_number = str(our_number % 2) + result_number
    our_number = our_number // 2 

print(int(result_number))
