with open('input.txt') as f:
    lines = map(lambda x: int(x), f.readlines())

window_sums = []
i = 0
window_start = 0
window_end = 2
counter = 0
while i < len(lines)-2:
    window_counter = 0
    for j in range(window_start, window_end+1):
        window_counter += lines[j]
    window_start += 1
    window_end += 1
    window_sums.append(window_counter)
    i +=1

i = 0
while i < len(window_sums)-1:
    crnLn = window_sums[i+1]
    if crnLn > window_sums[i]:
    	counter += 1
    i += 1
print(counter)