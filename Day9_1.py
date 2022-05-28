import sys
import math

# Input file
infile = open("Day9_input.txt", "r")

# Array to store height map from file
hmap = []

# Risk Level
r_level = 0

for l in infile:
    line_array = []
    line = l.strip()
    for x in line:
        line_array.append(int(x))
    hmap.append(line_array)

xmax = len(hmap[0])
ymax = len(hmap)

for y in range(ymax):
    for x in range(xmax):
        if x == 0:
            x0 = 10
        else:
            x0 = hmap[y][x-1]
        if x == xmax-1:
            x1 = 10
        else:
            x1 = hmap[y][x+1]
        if y == 0:
            y0 = 10
        else:
            y0 = hmap[y-1][x]
        if y == ymax-1:
            y1 = 10
        else:
            y1 = hmap[y+1][x]

        if hmap[y][x] < x0 and hmap[y][x] < x1 and hmap[y][x] < y0 and hmap[y][x] < y1:
            r_level += hmap[y][x] + 1

print(r_level)



