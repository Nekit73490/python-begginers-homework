
posd = open('file.txt','r')


posd = open('file.txt','r')


positions = []
for line in posd:
    positions.append(int(line))

list = [(i,i**2) for i in positions if i%2 == 0]



print(list)