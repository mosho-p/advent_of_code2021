import re

with open('day4.txt') as f:
    calls = f.readline().strip().split(',')
    boards = f.read().strip()

# Part 1
BINGO = ' '.join(['-1']*5)

def transpose(board):
    return '\n'.join([' '.join(y) for y in list(zip(*[x.split() for x in board.split('\n')]))])

# found = False
# for call in calls:
#     boards = re.sub(r'((?<=\s)|\A)' + call + r'((?=\s)|\Z)', '-1', boards)
#     for board in boards.split('\n\n'):
#         if BINGO in board or BINGO in transpose(board):
#             print(sum(map(int, board.replace('-1', '0').split())) * int(call))
#             found = True
#             break
#     if found:
#         break


# Part 2
found = False
done = False
boards = boards.replace('  ', ' ')
for call in calls:
    boards = re.sub(r'((?<=\s)|\A)' + call + r'((?=\s)|\Z)', '-1', boards)
    for board in boards.split('\n\n'):
        if BINGO in board or BINGO in transpose(board):
            if found:
                print(sum(map(int, boards.replace('-1', '0').split())) * int(call))
                done = True
                break
            boards = boards.replace(board, '').replace('\n'*4, '\n\n'*2).strip()
    if len(boards.split('\n\n')) == 1:
        print(boards)
        print(call)
        found = True
    if done:
        break

