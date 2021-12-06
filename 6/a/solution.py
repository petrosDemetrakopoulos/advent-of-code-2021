with open('test_input.txt') as f:
    lines = map(lambda x: x, f.readlines())

initial_fish = map(lambda x: int(x), lines[0].split(","))
print(initial_fish)

print("Initial state: " + str(initial_fish))
day = 0
for day in range(0, 18):
    i = 0
    for fish in initial_fish:
        if fish == 0:
            initial_fish[i] = 6
            initial_fish.append(9)
        else:
            initial_fish[i] = initial_fish[i] - 1
        i += 1
    print("After " + str(day + 1) + " days:" + str(initial_fish))
print("Total fish: " + str(len(initial_fish)))
        
