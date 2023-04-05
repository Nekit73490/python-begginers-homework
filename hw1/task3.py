
coord = input('enter coordinats of your point, seperated by comma ')
listalike = coord.split(',')

if int(listalike[1]) > 0:
    if int(listalike[0]) > 0:
        print(' its a first quarter')
    else:
        print(' its a second quarter')
else:
    if int(listalike[0]) > 0:
        print(' its a forth quarter')
    else:
        print(' its a third quarter')