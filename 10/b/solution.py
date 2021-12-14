import sys
import itertools
with open('input.txt') as f:
    lines = map(lambda x: x.replace("\n",""), f.readlines())

left = '<{(['
right = '>})]'
scores = {'>': 25137, '}': 1197,']': 57,')': 3}
stack = []
corruptedLines = []
sum = 0
for line in lines:
    corruptedLine = False
    for char in line:
        if char in left:
            stack.append(char)
        elif char in right:
            index = right.find(char)
            if stack[-1] != left[index]:
                corruptedLine = True
                break
            else:
                del stack[-1]
    if corruptedLine:
        corruptedLines.append(line)

score = 0
total_points = []
for line in non_corrupted_lines:
    stack = []
    missing = False
    for char in line.strip():
        if char in ('(','[','{','<'):
            stack.append(char)
        elif char == ')':
            if stack[-1] != '(':
                score += scores[')']
                missing = True
                break
            else:
                stack.pop()
        elif char == ']':
            if stack[-1] != '[':
                score += scores[']']
                missing = True
                break
            else:
                stack.pop()
        elif char == '}':
            if stack[-1] != '{':
                score += scores['}']
                missing = True
                break
            else:
                stack.pop()
        elif char == '>':
            if stack[-1] != '<':
                score += scores['>']
                missing = True
                break
            else:
                stack.pop()
    if not missing:
        s = 0
        points = {'(': 1, '[': 2,'{': 3,'<': 4}
        for c in reversed(stack):
            s = s*5 + points[c]
        total_points.append(s)
print(score)
total_points.sort()
print(total_points[len(total_points)//2])