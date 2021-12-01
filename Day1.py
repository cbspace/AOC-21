import sys

counter = 0

# Input file
infile = open("Day1_input.txt", 'r')

# Initialise previous
previous = int(infile.readline().strip())

# Read file entries
for line in infile.readlines():
    current = (int(line.strip()))
    if current > previous:
        counter += 1
    previous = current
infile.close()

print("The answer is", counter)
