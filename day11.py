with open('day11.txt') as f:
    raw = f.read().strip()

data = [[100]*12] + [[100] + list(map(int, x)) + [100] for x in raw.split()] + [[100]*12]

def power_up(data, i1=1, i2=10, j1=1, j2=10):
    for i in range(i1, i2+1):
        for j in range(j1, j2+1):
            data[i][j] += 1
    return data

def explode(data, flashes):
    for i in range(1, len(data)-1):
        for j in range(1, len(data)-1):
            if 50 > data[i][j] > 9:
                flashes += 1
                data[i][j] = 50
                data = power_up(data, i-1, i+1, j-1, j+1)
                data, flashes = explode(data, flashes)
    return data, flashes

# Part 1
# flashes = 0
# for _ in range(100):
#     data = power_up(data)
#     data, flashes = explode(data, flashes)
#     for i in range(1, 11):
#         for j in range(1, 11):
#             if data[i][j] >= 50:
#                 data[i][j] = 0
#
# print(flashes)

# Part 2
flashes = 0
steps = 0
dark = True
while dark:
    steps += 1
    data = power_up(data)
    data, flashes = explode(data, flashes)
    for i in range(1, 11):
        for j in range(1, 11):
            if data[i][j] >= 50:
                data[i][j] = 0
    dark = False
    for i in range(1, 11):
        for j in range(1, 11):
            if data[i][j] != 0:
                dark = True

print(steps)
