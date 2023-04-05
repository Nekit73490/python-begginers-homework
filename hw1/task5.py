coordsA = input('enter coordinates of point A, seperated by comma ')
coordsA = coordsA.split(',')

coordsA = [int(i) for i in coordsA]

coordsB = input('enter coordinates of point B, seperated by comma ')
coordsB = coordsB.split(',')

coordsB = [int(i) for i in coordsB]


if coordsA[0] > coordsB[0]:
    length = coordsA[0] - coordsB[0]
else:
    length = coordsB[0] - coordsA[0]


if coordsA[1] > coordsB[1]:
    hight = coordsA[1] - coordsB[1]
else:
    hight = coordsB[1] - coordsA[1]



from math import sqrt
distance = sqrt(hight**2 + length**2)
print(round(distance, 5))

