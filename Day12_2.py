import sys

# Array to store coordinates
coords = []

# Array of paths
path_array = []

# Populate path array
infile = open("Day12_input1.txt","r")
for l in infile:
    line_data = l.strip()
    line_array = line_data.split('-')
    coords.append(line_array)

# Create deep copy of array
def array_deep_copy(array_in):
    new_array = []
    for i in array_in:
        new_array.append(i)
    return new_array

# Create array of paths
# cave_in is index of current coordinates
# coord_index = 0 or 1 for current cave
def trace_path(cave_in, coord_index, current_path, travelled, second_pass_done):
    global path_count

    current_cave = coords[cave_in][coord_index]
    new_cave = coords[cave_in][~coord_index]
    current_path.append(current_cave)

    new_travelled = array_deep_copy(travelled)

    second_pass_done_update = second_pass_done

    if new_cave == "end":
        current_path.append("end")
        path_array.append(current_path)
    elif new_cave != "start":
        for c in coords:
            for ci in c:
                if ci == new_cave:
                    new_path = array_deep_copy(current_path)
                    if new_cave.isupper():
                        trace_path(coords.index(c), c.index(ci), new_path, new_travelled, second_pass_done_update)
                    else:
                        new_travelled.append(current_cave)
                        if new_travelled.count(new_cave) == 2:
                                second_pass_done_update = True
                        if second_pass_done_update == True:
                            if new_travelled.count(new_cave) < 1:
                                trace_path(coords.index(c), c.index(ci), new_path, new_travelled, True)
                        else:
                            if new_travelled.count(new_cave) <= 2:
                                trace_path(coords.index(c), c.index(ci), new_path, new_travelled, second_pass_done_update)
            
# Find the starting points
for c in coords:
    if c[0] == "start":
        current_path = []
        travelled = []
        trace_path(coords.index(c), 0, current_path, travelled, False)
    elif c[1] == "start":
        current_path = []
        travelled = []
        trace_path(coords.index(c), 1, current_path, travelled, False)

for a in path_array:
    print(a)

print(len(path_array))