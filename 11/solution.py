with open('input.txt') as f:
    lines = map(lambda x: x.replace("\n",""), f.readlines())

octopuses = map(lambda x: map(lambda y: int(y), x), lines)
already_flashed = map(lambda x: map(lambda y: False, x), lines)
steps = [1,2,3]
flash_counter = 0

def find_adjacent(pos):
    row = pos[0]
    col = pos[1]
    adjacent = []
    if row == 0 and col == 0: # top left
        adjacent += [[0,1],[1,0],[1,1]]
    elif row == 0 and col == len(octopuses[0]) - 1: # top right
        adjacent += [[0,len(octopuses[0]) - 2],[1,len(octopuses[0]) - 1],[1,len(octopuses[0]) - 2]]
    elif row == len(octopuses) - 1 and col == 0: # bottom left
        adjacent += [[len(octopuses) - 2,0], [len(octopuses) - 1,1], [len(octopuses) - 2,1]]
    elif row == len(octopuses) - 1 and col == len(octopuses[0]) - 1: # bottom right
        adjacent += [[len(octopuses) - 2,len(octopuses[0]) - 1], [len(octopuses) - 1,len(octopuses[0]) - 2], [len(octopuses) - 2,len(octopuses[0]) - 2]]
    elif row == 0: # top line
        adjacent += [[0, col-1],[0, col+1],[1,col],[1,col-1],[1,col+1]]
    elif row == len(octopuses) - 1: # bottom line
        adjacent += [[len(octopuses) -1, col -1], [len(octopuses) -1, col +1], [len(octopuses) - 2,col], [len(octopuses) - 2,col-1],[len(octopuses) - 2,col+1]]
    elif col == 0: # left line
        adjacent += [[row, 1], [row-1, 0], [row+1,0], [row-1, 1], [row+1, 1]]
    elif col == len(octopuses[0]) - 1: # right line
        adjacent += [[row, len(octopuses[0]) - 2],[row-1, len(octopuses[0]) - 2], [row-1, len(octopuses[0]) - 1], [row+1, len(octopuses[0]) - 1], [row+1, len(octopuses[0]) - 2]]
    else:
        top = [row - 1, col]
        bottom = [row + 1, col]
        left = [row, col-1]
        right = [row, col+1]
        top_left = [row-1, col-1]
        top_right = [row-1, col + 1]
        bottom_left = [row+1, col-1]
        bottom_right = [row+1, col+1]
        adjacent += [top,  bottom, left, right, top_left, top_right, bottom_left, bottom_right]
    return adjacent


def flash_octopus(pos):
    row = pos[0]
    col = pos[1]
    global flash_counter
    flash_counter += 1
    already_flashed[row][col] = True
    adjacents = find_adjacent([pos[0], pos[1]])
    octopuses[row][col] = 0
    for adj in adjacents:
        if already_flashed[adj[0]][adj[1]] == False:
            octopuses[adj[0]][adj[1]] += 1
            if octopuses[adj[0]][adj[1]] > 9: 
                flash_octopus([adj[0], adj[1]])

adj = []
for i in range(1,101):
    already_flashed = map(lambda x: map(lambda y: False, x), lines)
    for row in range(len(octopuses)):
        for col in range(len(octopuses[row])):
            octopuses[row][col] += 1

    for row in range(len(octopuses)):
        for col in range(len(octopuses[row])):
            if octopuses[row][col] > 9 and already_flashed[row][col] == False:
                flash_octopus([row, col])
                already_flashed[row][col] = True
    print("After step " + str(i))
    print(octopuses)

print(flash_counter)