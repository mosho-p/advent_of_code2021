from statistics import mode

with open('day3.txt') as f:
    data = f.read().split('\n')[:-1]

# Part 1
# gamma = ''.join([mode(x) for x in zip(*data)]).strip()
# epsilon = ''.join(['0' if x == '1' else '1' for x in gamma])
#
# print(int(gamma, 2) * int(epsilon, 2))

# Part 2
oxy = data.copy()
i = 0
while len(oxy) > 1:
    if i > len(oxy[0])-1:
        i = 0
    col = list(zip(*oxy))[i]
    save = '1' if col.count('1') >= col.count('0') else '0'
    oxy = [x for x in oxy if x[i]==save]
    i+=1

carb = data.copy()
i = 0
while len(carb) > 1:
    if i > len(carb[0])-1:
        i = 0
    col = list(zip(*carb))[i]
    save = '1' if col.count('1') < col.count('0') else '0'
    carb = [x for x in carb if x[i]==save]
    i+=1

print(int(oxy[0], 2) * int(carb[0], 2))
