from itertools import permutations
from functools import reduce
with open('input.txt') as f:
    lines = list(map(lambda x: x, f.readlines()))

def preprocess_data(data):
    new_lines = []
    i = 0
    for line in range(len(lines)):
        if i >= len(lines):
            break
        if "|" in lines[i]:
            signal = list(filter(lambda x: x!= '|' and x!= '\n', lines[i].replace(" |\n","").split(" ")))
            numbers = lines[i + 1].replace("\n","").split(" ")
            new_lines.append([signal, numbers])
        i += 2
    return new_lines


output = list(map(lambda x: x[1], preprocess_data(lines)))
signals = list(map(lambda x: x[0], preprocess_data(lines)))

solution = 0
valid_patterns = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}
all_possible_signals = permutations("abcdefg")
all_possible_signals = list(map(lambda x: "".join(x), all_possible_signals))

for i in range(len(signals)):
    signal = signals[i]
    out = output[i]
    for pos_signal in all_possible_signals:
        correct_output_mapping = str.maketrans("abcdefg", pos_signal)
        correct_signal = ["".join(sorted(("".join(sig)).translate(correct_output_mapping))) for sig in signal]
        correct_output = ["".join(sorted(op.translate(correct_output_mapping))) for op in out]
        
        if all(code in valid_patterns for code in correct_signal):
            solution += int("".join(str(valid_patterns[code]) for code in correct_output))            
            break

print(solution)


