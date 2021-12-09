with open('input.txt') as f:
    lines = map(lambda x: x, f.readlines())

def preprocess_data(data):
    new_lines = []
    i = 0
    for line in range(len(lines)):
        if i >= len(lines):
            break
        if "|" in lines[i]:
            signal = filter(lambda x: x!= '|' and x!= '\n', lines[i].replace(" |\n","").split(" "))
            numbers = lines[i + 1].replace("\n","").split(" ")
            new_lines.append([signal, numbers])
        i += 2
    return new_lines

all_output_vals = map(lambda x: x[1], preprocess_data(lines))
all_output_vals = reduce(lambda x,y: x+y, all_output_vals)

counter = 0

for val in all_output_vals:
    if len(val) in (2,3,4,7):
        print("counted " + val)
        counter += 1
print(counter)