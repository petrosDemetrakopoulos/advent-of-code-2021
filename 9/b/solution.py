with open('input.txt') as f:
    lines = map(lambda x: x.replace("\n",""), f.readlines())

matrix = map(lambda x: map(lambda y: int(y), list(x)), lines)
low_points = []

def find_adjacent(point, matrix):
    x = point[0]
    y = point[1]
    if x == 0 and y == 0:
        # top left corner
        return[[0,1],[1,0]]
    if x == 0 and y == len(matrix[0]) - 1:
        #top right corner
        return [[0, len(matrix[0]) - 2], [1, len(matrix[0]) - 1]]
    if x == len(matrix) - 1 and y == 0:
        #bottom left corner
        return[[len(matrix) - 2, 0], [1,len(matrix) - 1]]
    if x == len(matrix) - 1 and y == len(matrix[0]) - 1:
        #bottom right corner
        return [[len(matrix) - 1, len(matrix[0]) - 2], [len(matrix) - 2,len(matrix[0]) - 1]]
    if y == 0:
        # left edge
        up = [x-1, y]
        down = [x+1, y]
        right = [x,y+1]
        return [up, down, right]
    if y == len(matrix[0]) - 1:
        # right edge
        up = [x-1, y]
        down = [x+1, y]
        left = [x, y-1]
        return [up, down, left]
    if x == 0:
        # top edge
        down = [x+1, y]
        left = [x, y-1]
        right = [x,y+1]
        return [down, left, right]
    if x == len(matrix) - 1:
        # down edge
        up = [x-1, y]
        left = [x, y-1]
        right = [x,y+1]
        return [up, left, right]
    if x in range(1, len(matrix) -1) and y in range(1, len(matrix[0]) -1):
        up = [x-1, y]
        down = [x+1,y]
        left = [x, y-1]
        right = [x,y+1]
        return [up, down, left, right]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        crn_point = matrix[i][j]
        adjacents = find_adjacent([i, j], matrix)
        is_min = True
        for adjacent in adjacents:
            if matrix[adjacent[0]][adjacent[1]] <= crn_point:
                is_min = False
                break
        if is_min:
            low_points.append([i, j])

low_point_vals = map(lambda x: matrix[x[0]][x[1]], low_points)

def find_basin_for_point(point, matrix):
        adjacents = find_adjacent(point, matrix)
        basin = [point]
        if matrix[point[0]][point[1]] == 9:
            return []
        for adjacent in adjacents:
            adj_x = adjacent[0]
            adj_y = adjacent[1]
            if matrix[adj_x][adj_y] in range(matrix[point[0]][point[1]] + 1,9):
                basins_for_point = find_basin_for_point([adj_x, adj_y], matrix)
                basin.append(basins_for_point)
        return basin

print("low points: " + str(low_points))
all_basins = []

for point in low_points:
    all_basins.append(find_basin_for_point(point, matrix))

def count_basin_size(basin,already_count=[], count=0):
    if isinstance(basin[0],int):
        if basin not in already_count:
            already_count.append(basin)
            count += 1
        return count
    else:
        total = 0
        for i in range(len(basin)):
            total += count_basin_size(basin[i], already_count, count)
        return total

sizes = []
for basin in all_basins:
    sizes.append(count_basin_size(basin))
sorted = sorted(sizes, reverse=True)
print(sorted[0] * sorted[1] * sorted[2])