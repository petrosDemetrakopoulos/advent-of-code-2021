with open('input.txt') as f:
    lines = map(lambda x: [x.replace("\n","").split(" ")[0], int(x.replace("\n","").split(" ")[1])], f.readlines())

depth = 0
horizontal = 0
aim = 0

for move in lines:
    if move[0] == 'forward':
        horizontal += move[1]
        depth += aim * move[1]
    elif move[0] == 'down':
        #depth += move[1]
        aim += move[1]
    elif move[0] == 'up':
        #depth -= move[1]
        aim -= move[1]
print("horizontal: " + str(horizontal) + " depth: " + str(depth))
