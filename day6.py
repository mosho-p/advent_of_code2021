with open('day6.txt') as f:
    data = f.readline()

fish = {x: data.count(str(x)) for x in range(9)}

def count_fish(days):
    for _ in range(days):
        fish = {(k-1) % 9: v if (k-1) != 6 else v + fish[0] for k, v in fish.items()}

print(sum(fish.values()))
