with open('input.txt') as f:
    lines = map(lambda x: int(x), f.readlines())

length = len(lines)
i = 0
counter = 0
while i < length-1:
    crnLn = lines[i+1]
    if crnLn > lines[i]:
    	counter += 1
    i += 1
print(counter)