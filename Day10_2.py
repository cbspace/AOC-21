import sys

# Input lines to be parsed
line_array = []

# Valid characters
open_brackets = ['(','[','{','<']
closed_brackets = [')',']','}','>']

# Points
points_table = []

# Input file
infile = open("Day10_input.txt", "r")
for l in infile:
	line_array.append(l.strip())

for line in line_array:
	lstack = []
	total_points = 0
	for c in line:
		if c in open_brackets:
			lstack.append(c)
		elif c in closed_brackets:
			if open_brackets[closed_brackets.index(c)] != lstack.pop():
				total_points += points_table[closed_brackets.index(c)]
				continue
	for s in reversed(lstack):
		print(lstack.pop())
		total_points *= 5
		total_points += open_brackets.index(s)+1
		line_scores.append(total_points)

line_scores.sort()
print(line_scores[len(line_scores/2)])
