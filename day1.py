with open('day1.txt') as f:
    l = list(map(int, f.readlines()))

# Part 1
i = 0
for a, b in zip(l[:-1], l[1:]):
    if b > a:
        i += 1

# Part 2
i = 0
for a, b in zip(l[:-3], l[3:]):
    if b > a:
        i += 1
print(i)