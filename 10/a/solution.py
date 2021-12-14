with open('test_input.txt') as f:
    lines = map(lambda x: x.replace("\n",""), f.readlines())

left = '<{(['
right = '>})]'
scores = {'>': 4, '}': 3,']': 2,')': 1}
corrupted_lines = []
for line in lines:
    stack = []
    corrupted = False
    for char in line:
        if char in left:
            stack.append(char)
        elif char in right:
            index = right.find(char)
            if stack[-1] != left[index]:
                corrupted = True
                break
            else:
                del stack[-1]
    if corrupted:
        corrupted_lines.append(line)


incomplete_lines = [x for x in lines if x not in corrupted_lines]
print(incomplete_lines)