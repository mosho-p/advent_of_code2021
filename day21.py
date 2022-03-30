player1 = 7
score1 = 0
player2 = 5
score2 = 0
dice = 1
rolls = 0

# Part 1
# while True:
#     player1 = ((player1 + dice * 3 + 3 - 1) % 10) + 1
#     score1 += player1
#     dice = ((dice + 2) % 100) + 1
#     rolls += 3
#     if score1 > 1000:
#         print(rolls * score2)
#         break
#     player2 = ((player2 + dice * 3 + 3 - 1) % 10) + 1
#     score2 += player2
#     dice = ((dice + 2) % 100) + 1
#     rolls += 3
#     if score2 > 1000:
#         print(rolls * score1)
#         break

# Part 2
# ends up:
# +3 1
# +4 3
# +5 6
# +6 7
# +7 6
# +8 3
# +9 1


def move(start, roll):
    next_spot = (start + roll) % 10
    return 10 if next_spot == 0 else next_spot


def play(pos, score, turn, roll, value):
    next_pos = (move(pos[0], roll), pos[1]) if turn == 0 else (pos[0], move(pos[1], roll))
    next_score = (score[0] + next_pos[0], score[1]) if turn == 0 else (score[0], score[1] + next_pos[1])
    next_turn = (turn + 1) % 2
    if next_score[0] >= 21:
        return value, 0
    if next_score[1] >= 21:
        return 0, value
    return [sum(x) for x in zip(
        play(next_pos, next_score, next_turn, 3, value * 1),
        play(next_pos, next_score, next_turn, 4, value * 3),
        play(next_pos, next_score, next_turn, 5, value * 6),
        play(next_pos, next_score, next_turn, 6, value * 7),
        play(next_pos, next_score, next_turn, 7, value * 6),
        play(next_pos, next_score, next_turn, 8, value * 3),
        play(next_pos, next_score, next_turn, 9, value * 1),
    )]


starts = (player1, 0)
scores = (0, -5)
print(play(starts, scores, turn=1, roll=5, value=1))
