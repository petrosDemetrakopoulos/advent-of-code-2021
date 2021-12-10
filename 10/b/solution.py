with open('input.txt') as f:
    lines = map(lambda x: x.replace("\n",""), f.readlines())

left = '<{(['
right = '>})]'
scores = {'>': 25137, '}': 1197,']': 57,')': 3}
stack = []
sum = 0
for line in lines:
    for char in line:
        if char in left:
            stack.append(char)
        elif char in right:
            index = right.find(char)
            if stack[-1] != left[index]:
                sum += scores[char]
                break
            else:
                del stack[-1]
print(sum)