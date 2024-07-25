#to make 2048 game
import numpy
import random
import cell

N=4
# don't need seed here
#instantiates the map
grid = numpy.empty((N,N), dtype=cell)
for i in range(N):
    for j in range(N):
        grid[i,j] = cell[i,j]

count=0
while(count <2):
    x = random.randrange(0, N)
    y = random.randrange(0,N)
    count+=1
