with open('input.txt') as f:
    lines = map(lambda x: x, f.readlines())

positions = lines[0].split(",")
positions = map(int,positions)
positions_of_alignment = []

def calculate_fuel(pos, pos_align):
    fuel = 0
    if pos > pos_align:
        for i in range(pos - pos_align + 1):
            fuel += i
    elif pos_align > pos:
        for i in range(pos_align - pos + 1):
            fuel += i
    else: #pos_align == pos
        fuel += 0
    return fuel

positions_max = max(positions)
for pos_of_align in range(positions_max):
    fuel = 0
    for pos in range(len(positions)):
        fuel += calculate_fuel(positions[pos], pos_of_align)
    print("fuel for align pos " + str(pos_of_align) + " = " + str(fuel))
    positions_of_alignment.append({pos_of_align: fuel})

fuel_for_alignment_pos = map(lambda x: x[x.keys()[0]], positions_of_alignment)
print(sorted(fuel_for_alignment_pos)[0])