with open('day7.txt') as f:
    data = eval(f.readline())

# Part 1
median = sorted(data)[len(data)//2]
print(sum([abs(x - median) for x in data]))


# Part 2
def fuel_usage(start, end):
    return (abs(start - end) + 1) * abs(start - end) // 2


# It's like theres a number at every point between the number and the target
target = sum(data)//len(data)

print(min(sum([fuel_usage(x, target) for x in data]), sum([fuel_usage(x, target + 1) for x in data])))
