with open('day10.txt') as f:
    data = f.read().strip().split()

# start from the beginning and record openings
# when you find a closing pop openings, if it's a mismatch record it

matches = {'(': ')', '[': ']', '{': '}', '<': '>'}
# Part 1
# values = {')': 3, ']': 57, '}': 1197, '>': 25137}

# illegals = []
# for line in data:
#     openings = []
#     for char in line:
#         if char in '([{<':
#             openings.append(char)
#         else:
#             latest = openings.pop()
#             if matches[latest] != char:
#                 illegals.append(values[char])
#
# print(sum(illegals))

# Part 2
values = {')': 1, ']': 2, '}': 3, '>': 4}

points = []
for line in data:
    openings = []
    skip = False
    for char in line:
        if char in '([{<':
            openings.append(char)
        else:
            latest = openings.pop()
            if matches[latest] != char:
                skip = True
                break
    if skip:
        continue
    score = 0
    for o in openings[::-1]:
        score *= 5
        score += values[matches[o]]
    points.append(score)

print(sorted(points)[len(points)//2])
