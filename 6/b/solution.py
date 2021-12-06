with open('input.txt') as f:
    lines = map(lambda x: x, f.readlines())

initial_fish = map(lambda x: int(x), lines[0].split(","))
print(initial_fish)

print("Initial state: " + str(initial_fish))
state = {0: 0, 1: 0, 2: 0, 3: 0, 4:0 ,5: 0, 6: 0, 7: 0, 8:0}
for i in range(len(initial_fish)):
    state[initial_fish[i]] += 1

print("init state = " + str(state))
for day in range(0, 256):
    new_state = {0: 0, 1: 0, 2: 0, 3: 0, 4:0 ,5: 0, 6: 0, 7: 0, 8:0}
    for i in range(1,len(state.keys())):
        new_state[i-1] = state[i]
    new_state[8] = state[0]
    new_state[6] += state[0]
    state = new_state
print("Total fish: " + str(sum(state.values())))