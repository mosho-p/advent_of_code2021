from collections import defaultdict


with open('day14.txt') as f:
    start = f.readline().strip()
    f.readline()
    table = {line[:2]: line[0] + line[-2] + line[1] for line in f.readlines()}


polymer = start
for _ in range(10):
    temp = polymer[0]
    for a, b in zip(polymer[:-1], polymer[1:]):
        temp += table.get(a+b, a+b)[1:]
    polymer = temp

counts = [polymer.count(x) for x in set(polymer)]

print(max(counts) - min(counts))

# keep track of how many pairs there are. If OH:3 and we insert B, then add 3 to OB and 3 to BH and subtract 3 from OH
# for counting, can we tell when an OB and a BN are the same B or different Bs? Every letter is duplicated except the first and last

pairs = defaultdict(lambda: 0)
for a, b in zip(start[:-1], start[1:]):
    pairs[a+b] += 1

for _ in range(40):
    temp = pairs.copy()
    for k, v in pairs.items():
        if k not in table:
            continue
        temp[table[k][:2]] += v
        temp[table[k][1:]] += v
        temp[k] -= v
    pairs = temp

# add 1 to F and C, then divide everything by 2

counts = defaultdict(lambda: 0)
counts['F'] = 1
counts['C'] = 1

for k, v in pairs.items():
    counts[k[0]] += v
    counts[k[1]] += v

print(max(counts.values())/2 - min(counts.values())/2)