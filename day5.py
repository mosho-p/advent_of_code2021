with open('day5.txt') as f:
    data = [sorted(eval(f"({line.replace(' -> ', '), (')})")) for line in f.readlines()]

# Part 1
# drop diagonals
orthogs = [x for x in data if x[0][0] == x[1][0] or x[0][1] == x[1][1]]
diags = [x for x in data if x[0][0] != x[1][0] and x[0][1] != x[1][1]]
# total max(x) * max(y) points
# sort by x1, x2
# if x1 = x2 then break into individual points at each y

points = set()
dupes = set()
for ((x1, y1), (x2, y2)) in orthogs:
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if (x, y) in points:
                dupes.add((x, y))
            else:
                points.add((x, y))

for ((x1, y1), (x2, y2)) in diags:
    for i in range(x2 - x1 + 1):
        p = (x1 + i, y1 + i if y2 > y1 else y1 - i)
        if p in points:
            dupes.add(p)
        else:
            points.add(p)

print(len(dupes))
