

for x in range(0,2):
    # print(x)
    for y in range(0,2):
        # print(y)
        for z in range(0,2):
            # print(z)
            print((not(x or y or z)) == ((not x) and (not y) and( not z)))
