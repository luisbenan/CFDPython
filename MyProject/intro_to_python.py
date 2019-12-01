# <-- comments in python are denoted by the pound sign, like this one

import numpy          # we import the array library
from matplotlib import pyplot   # import plotting library

myarray = numpy.linspace(0, 5, 10)
myarray

a = 5
b = 'five'
c = 5.0

type(a)
type(b)
type(c)

for i in range(5):
    print("Hi \n")


for i in range(3):
    for j in range(3):
        print(i, j)

    print("This statement is within the i-loop, but not the j-loop")

myvals = numpy.array([1, 2, 3, 4, 5])
myvals

myvals[0], myvals[4]

print(myvals[0:3])

# Assigning Array Variables

a = numpy.linspace(1, 5, 5)
a

b = a
b

a[2] = 17
a
b

c = a.copy()
a
c
