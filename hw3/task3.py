working_list = input('enter your list of float numbers, separated by commas ')

working_list = working_list.split(',')

count = 0

for i in working_list:
    if "." in i :
        if count < 1 :
            start = i.find(".") + 1
            our_min = (float(i[start:])/(10**len(i[start:])))
            our_max = (float(i[start:])/(10**len(i[start:])))
            # print(our_max, ' ', our_min)
            count = 1
        else :
            start = i.find(".") + 1
            if (float(i[start:])/(10**len(i[start:]))) < our_min:
                our_min = (float(i[start:])/(10**len(i[start:])))
            if (float(i[start:])/(10**len(i[start:]))) > our_max: 
                our_max = (float(i[start:])/(10**len(i[start:])))
            # print(our_max, ' ', our_min)

print(our_max - our_min)
