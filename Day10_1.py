import sys

# Input lines to be parsed
line_array = []

# Stack for parsing
lstack = []

# Valid characters
open_brackets = ['(','[','{','<']
closed_brackets = [')',']','}','>']

# Input file
infile = open("Day10_input.txt", "r")
for l in infile:
	line_array.append(l.strip())

for line in line_array:
    for c in line:
        if c in open_brackets:
            lstack.append(c)
        elif c in closed_brackets:
            if c == lstack.pop:
                print('ok')
            else:
                print('error')