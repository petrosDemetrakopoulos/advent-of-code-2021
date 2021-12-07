with open('input.txt') as f:
    lines = map(lambda x: x, f.readlines())

positions = lines[0].split(",")
positions = map(int,positions)

positions_of_alignment = []

for pos_of_align in range(len(positions)):
    fuel = 0
    for pos in range(len(positions)):
        fuel += abs(positions[pos] - positions[pos_of_align])
    print("fuel for align pos " + str(positions[pos_of_align]) + " = " + str(fuel))
    positions_of_alignment.append({positions[pos_of_align]: fuel})

fuel_for_alignment_pos = map(lambda x: x[x.keys()[0]], positions_of_alignment)
print(sorted(fuel_for_alignment_pos)[0])