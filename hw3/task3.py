working_list = input('enter your list of float numbers, separated by commas ')

working_list = working_list.split(',')

count = 0

def scaling(curent_number, starting_pos):
  return((float(curent_number[starting_pos:])/(10**len(curent_number[starting_pos:]))))

for i in working_list:
    if "." in i :
        if count < 1 :
            start = i.find(".") + 1
            our_min = scaling(i,start)
            our_max = scaling(i,start)
            # print(our_max, ' ', our_min)
            count = 1
        else :
            start = i.find(".") + 1
            if scaling(i,start) < our_min:
                our_min = scaling(i,start)
            if scaling(i,start) > our_max: 
                our_max = scaling(i,start)
            # print(our_max, ' ', our_min)

print(our_max - our_min)
