with open('day2.txt') as f:
    l = f.readlines()

# Part 1
# print(sum([int(s.split()[1]) for s in l if 'forward' in s]) * (sum([int(s.split()[1]) for s in l if 'down' in s])-sum([int(s.split()[1]) for s in l if 'up' in s])))

# Part 2
aim = 0
depth = 0
hor = 0
for a in l:
    dr, val = a.split()
    val = int(val)
    if dr == 'forward':
        depth += aim * val
        hor += val
    if dr == 'up':
        aim -= val
    if dr == 'down':
        aim += val
print(depth * hor)
