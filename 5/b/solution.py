with open('input.txt') as f:
    lines = map(lambda x: x, f.readlines())

def preprocess_data(lines):
    lines = map(lambda x: x.replace("\n","").replace(" ","").split("->"), lines)
    for i in range(len(lines)):
        for p in range(len(lines[i])):
            lines[i][p] = map(lambda x: int(x), lines[i][p].split(","))
    return lines

data = preprocess_data(lines)
def find_max_x(data):
    all_x = map(lambda x: map(lambda y: y[0], x), data)
    all_x = reduce(lambda x,y: x+y, all_x)
    return max(all_x)

def find_max_y(data):
    all_y = map(lambda x: map(lambda y: y[1], x), data)
    all_y = reduce(lambda x,y: x+y, all_y)
    return max(all_y)

def calculate_lamda(line):
    if line[0][0] != line[1][0]:
        return (line[0][1] - line[1][1]) / (line[0][0] - line[1][0])
    else:
        return 0

diagonal_lines = map(lambda x: x if calculate_lamda(x) in [-1,1] else [], data)
diagonal_lines = filter(lambda x: len(x) > 0, diagonal_lines)

filtered_lines = filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], data)

matrix = []
max_x = find_max_x(data)
max_y = find_max_y(data)

for i in range(0,max_x + 1):
    matrix.append([])
    for j in range(0,max_y + 1):
        matrix[i].append(0)

def points_of_line(line):
    points_covered = []
    if line[0][0] == line[1][0]: #horizontal
        step = 1 if line[1][1] >= line[0][1] else -1
        for i in range(line[0][1], line[1][1] + step, step):
            points_covered.append([line[0][0], i])
    elif line[0][1] == line[1][1]: #vertical
        step = 1 if line[1][0] >= line[0][0] else -1
        for i in range(line[0][0], line[1][0] + step, step):
            points_covered.append([i, line[0][1]])
    return points_covered

all_points_covered = map(lambda x: points_of_line(x), filtered_lines)

for line in diagonal_lines:
    points_covered = []
    if line[0][0] == line[0][1] and line[1][0] == line[1][1]: #horizontal
        step = 1 if line[1][1] >= line[0][1] else -1
        for i in range(line[0][0], line[1][1] + step, step):
            points_covered.append([i,i])
    elif line [1][1] == line [0][0] and line[1][0] == line[0][1]:
        step = -1 if line[1][1] <= line[0][1] else 1
        j = 0
        for i in range(line[0][1], line[1][1] + step, step):
            sign = 1 if line[1][1] <= line[0][1] else -1
            points_covered.append([line[0][0] + sign*j, line[0][1] - sign*j])
            j += 1
    elif line[0][0] >= line[1][0] and line[0][1] >= line[1][1]:
        j = 0
        for i in range(line[0][0], line[1][0] -1, -1):
            points_covered.append([i, line[0][1] - j])
            j += 1
    elif line[0][0] <= line[1][0] and line[0][1] >= line[1][1]:
        j = 0
        for i in range(line[0][0], line[1][0] + 1, 1):
            points_covered.append([i, line[0][1] - j])
            j += 1
    elif line[0][0] >= line[1][0] and line[0][1] <= line[1][1]:
        j = 0
        for i in range(line[0][0], line[1][0] -1, -1):
            points_covered.append([i, line[0][1] + j])
            j += 1
    elif line[0][0] <= line[1][0] and line[0][1] <= line[1][1]:
        j = 0
        for i in range(line[0][0], line[1][0] + 1, 1):
            points_covered.append([i, line[0][1] + j])
            j += 1
    all_points_covered.append(points_covered)

all_points_covered = reduce(lambda x,y: x+y, all_points_covered)  

for point in all_points_covered:
    x = point[0]
    y = point[1]
    matrix[x][y] += 1

flattened_matrix = reduce(lambda x,y: x + y, matrix)
counter = sum(1 for x in flattened_matrix if x > 1)
print(counter)