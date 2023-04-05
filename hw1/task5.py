coordsA = input('enter coordinates of point A, seperated by comma ')
coordsA = coordsA.split(',')
coordsB = input('enter coordinates of point B, seperated by comma ')
coordsB = coordsB.split(',')


if int(coordsA[0]) > int(coordsB[0]):
    length = int(coordsA[0]) - int(coordsB[0])
else:
    length = int(coordsB[0]) - int(coordsA[0])


if int(coordsA[1]) > int(coordsB[1]):
    hight = int(coordsA[1]) - int(coordsB[1])
else:
    hight = int(coordsB[1]) - int(coordsA[1])



from math import sqrt
distance = sqrt(hight**2 + length**2)
print(round(distance, 5))

