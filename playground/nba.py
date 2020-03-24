# ranks

import numpy

rating = [1711, 1728, 1617, 1539, 1709, 1652, 1629, 1640, 1618, 1585, 1578, 1610, 1524, 1549, 1480, 1475, 1407,
              1440, 1526, 1453, 1416, 1497, 1430, 1323, 1380, 1410, 1351, 1352, 1302, 1295]

eli = [53.7, 49.4, 35.9, 32.8, 30.3, 29.0, 29.2, 28.3, 25.7, 25.9, 25.8, 22.8, 20.5, 20.5, 17.9, 17.1]
eli2 = [35.9, 32.8, 30.3, 29.0, 29.2, 28.3, 25.7, 25.9, 25.8, 22.8, 20.5, 20.5]

print(len(eli2))
print("Mean rating: ")
avg = numpy.mean(eli2)
print(avg)

print("Median rating:")
med = numpy.median(eli2)
print(med)

print("Standard deviation:")
stdev = numpy.std(eli2)
print(stdev)
