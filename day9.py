with open('day9.txt') as f:
    raw = f.read().strip()

framed = [[9] * (len(raw.split()[0]) + 2)] + [[9] + list(map(int, s)) + [9] for s in raw.split()] + [[9] * (len(raw.split()[0]) + 2)]
height_map = framed.copy()

# Part 1
# local_mins = []
# for x in range(1, len(framed[0]) - 1):
#     for y in range(1, len(framed) - 1):
#         if framed[y][x] < framed[y-1][x] \
#                 and framed[y][x] < framed[y+1][x] \
#                 and framed[y][x] < framed[y][x-1] \
#                 and framed[y][x] < framed[y][x+1]:
#             local_mins.append(framed[y][x] + 1)
#
# print(sum(local_mins))

# Part 2
# replace first min with 'a' (or 10)
# replace everything touching 'a' (or 10) that isn't a 9 with 'a' (or 10)
# when there's nothing else to replace, move on to next min


def find_min():
    for x in range(1, len(height_map[0]) - 1):
        for y in range(1, len(height_map) - 1):
            if height_map[y][x] < height_map[y-1][x] \
                    and height_map[y][x] < height_map[y+1][x] \
                    and height_map[y][x] < height_map[y][x-1] \
                    and height_map[y][x] < height_map[y][x+1]\
                    and height_map[y][x] != 9:
                return y, x
    return -1, -1


def replace_neighbor(x, y, basin):
    found = False
    if height_map[y-1][x] < 9:
        height_map[y-1][x] = basin
        replace_neighbor(x, y-1, basin)
        found = True
        basins[basin] += 1
    if height_map[y+1][x] < 9:
        height_map[y+1][x] = basin
        replace_neighbor(x, y+1, basin)
        found = True
        basins[basin] += 1
    if height_map[y][x-1] < 9:
        height_map[y][x-1] = basin
        replace_neighbor(x-1, y, basin)
        found = True
        basins[basin] += 1
    if height_map[y][x+1] < 9:
        height_map[y][x+1] = basin
        replace_neighbor(x+1, y, basin)
        found = True
        basins[basin] += 1
    return found

basin_num = 10
basins = {basin_num: 0}
y, x = find_min()
while True:
    if y == -1:
        break
    found = replace_neighbor(x, y, basin_num)
    if not found:
        basin_num += 1
        basins[basin_num] = 0
        y, x = find_min()

print(sorted(basins.values())[-1] * sorted(basins.values())[-2] * sorted(basins.values())[-3])
