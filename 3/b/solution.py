with open('input.txt') as f:
    lines = map(lambda x: list(x.replace("\n","")), f.readlines())

epsilon_rate = []
gamma_rate = []
def calculate_gamma_rate(lines):
    gamma_rate = []
    for i in range(0,len(lines[0])):
        zeros = 0
        ones = 0
        for line in lines:
            zeros += 1 if line[i] == 0 else 0
            ones += 1 if line[i] == 1 else 0
        if ones > zeros:
            gamma_rate.append(1)
            epsilon_rate.append(0)
        elif ones == zeros:
            gamma_rate.append(1)
            epsilon_rate.append(0)
        else:
            gamma_rate.append(0)
            epsilon_rate.append(1)
    return gamma_rate

def calculate_epsilon_rate(lines):
    epsilon_rate = []
    for i in range(0,len(lines[0])):
        zeros = 0
        ones = 0
        for line in lines:
            zeros += 1 if line[i] == 0 else 0
            ones += 1 if line[i] == 1 else 0
        if ones > zeros:
            epsilon_rate.append(0)
        elif ones == zeros:
            epsilon_rate.append(0)
        else:
            epsilon_rate.append(1)
    return epsilon_rate

def calculate_oxygen(lines,i):
    gamma_rate = calculate_gamma_rate(lines)
    lines_to_remove = []
    if len(lines) > 1:
        for line in lines:
            if line[i] != gamma_rate[i]:
                lines_to_remove.append(line)
        return calculate_oxygen([x for x in lines if x not in lines_to_remove], i + 1)
    else:
        return [x for x in lines if x not in lines_to_remove]


def calculate_CO2(lines,i):
    epsilon_rate = calculate_epsilon_rate(lines)
    lines_to_remove = []
    if len(lines) > 1:
        for line in lines:
            if line[i] != epsilon_rate[i]:
                lines_to_remove.append(line)
        return calculate_CO2([x for x in lines if x not in lines_to_remove], i + 1)
    else:
        return [x for x in lines if x not in lines_to_remove]

def format_result(result):
    result = [map(str,x) for x in result]
    result = result[0]
    result = "".join(result)
    return int(result,2)

lines = [map(int,x) for x in lines]
oxygen = calculate_oxygen(lines,0)
oxygen = format_result(oxygen)
print("Oxygen = " + str(oxygen))

co_2 = calculate_CO2(lines,0)
co_2 = format_result(co_2)
print("C02 = " + str(co_2))
