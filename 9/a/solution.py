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
    if x == 0 and y == len(matrix) - 1:
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
        up = [x, y-1]
        down = [x,y+1]
        left = [x-1, y]
        right = [x+1,y]
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
risk_level = map(lambda x: 1 + x, low_point_vals)

print(sum(risk_level))