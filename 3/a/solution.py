with open('input.txt') as f:
    lines = map(lambda x: list(x.replace("\n","")), f.readlines())

gamma_rate = []
epsilon_rate = []
for i in range(0,len(lines[0])):
    zeros = 0
    ones = 0
    for line in lines:
        zeros += 1 if line[i] == '0' else 0
        ones += 1 if line[i] == '1' else 0
    gamma_rate.append(1 if ones > zeros else 0)
    epsilon_rate.append(1 if ones < zeros else 0)
gamma_rate = list(map(str,gamma_rate))
epsilon_rate = list(map(str,epsilon_rate))
gamma_rate_str = "".join(gamma_rate)
epsilon_rate_str = "".join(epsilon_rate)
print("gamma decimal: " + str(int(gamma_rate_str,2)))
print("epsilon decimal: " + str(int(epsilon_rate_str,2)))