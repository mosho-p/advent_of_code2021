# Part 1
# with open('day8.txt') as f:
#     raw = f.read().strip()

# part1 = []
# for line in raw.split('\n'):
#     part1.extend(line.split(' | ')[1].split())
#
# print(len([x for x in part1 if len(x) in (2, 3, 4, 7)]))

# Part 2
LENGTHS = {2: {1}, 3: {7}, 4: {4}, 5: {2, 3, 5}, 6: {6, 9}, 7: {8}}


class ReadOut:
    def __init__(self, line):
        self.out = list(map(lambda x: ''.join(sorted(x)), line.split(' | ')[1].split()))
        self.digits = set(map(lambda x: ''.join(sorted(x)), line.replace(' |', '').split()))
        self.known_nums = {}
        self.known_strs = {}

        self.get_knowns()
        maybe3 = [set(x) for x in self.digits if len(x) == 5]
        if len(maybe3) == 3:
            self.get3_another_way(maybe3)
            self.get9()
        if 4 in self.known_nums:
            self.get0()
            self.get9()
        if 1 in self.known_nums or 7 in self.known_nums:
            self.get3()
            self.get6()
        self.get2()
        self.get5()
        self.get6()
        self.get9()
        self.get0()

    def get_knowns(self):
        for x in self.digits:
            if len(x) == 2:
                self.known_nums[1] = set(x)
                self.known_strs[x] = '1'
            elif len(x) == 3:
                self.known_nums[7] = set(x)
                self.known_strs[x] = '7'
            elif len(x) == 4:
                self.known_nums[4] = set(x)
                self.known_strs[x] = '4'
            elif len(x) == 7:
                self.known_nums[8] = set(x)
                self.known_strs[x] = '8'

    def get_out_int(self):
        return int(''.join([self.known_strs[x] for x in self.out]))

    def get0(self):
        for x in self.digits:
            if len(x) != 6:
                continue
            if not set(x).issuperset(self.known_nums.get(4, set('z'))) \
                    and set(x).issuperset(self.known_nums.get(1) or self.known_nums.get(7, set('z'))):
                self.known_nums[0] = set(x)
                self.known_strs[x] = '0'

    def get2(self):
        # diff of certain numbers are certain things (possibly with `and 3 in self.known_nums`)
        # (1 or 7) - 6 is in there
        for x in self.digits:
            if len(x) != 5:
                continue
            if (set(x).issuperset((self.known_nums.get(1) or self.known_nums.get(7, set())) - (self.known_nums.get(6) or set('abcdefg')))\
                    and self.known_strs.get(x) != '3')\
                    or (set(x).issubset(self.known_nums.get(9, set('z'))) and self.known_strs.get(x) != '3')\
                    or len(set(x) - self.known_nums.get(4, set())) == 3:
                self.known_nums[2] = set(x)
                self.known_strs[x] = '2'

    def get3(self):
        # 1 or 7 is subset
        for x in self.digits:
            if len(x) != 5:
                continue
            if set(x).issuperset(self.known_nums.get(1) or self.known_nums.get(7, set('z'))):
                self.known_nums[3] = set(x)
                self.known_strs[x] = '3'

    def get3_another_way(self, potentials):
        if len(potentials[0] - potentials[1] - potentials[2]) == 0:
            self.known_nums[3] = set(potentials[0])
            self.known_strs[''.join(sorted(potentials[0]))] = '3'
        if len(potentials[1] - potentials[0] - potentials[2]) == 0:
            self.known_nums[3] = set(potentials[1])
            self.known_strs[''.join(sorted(potentials[1]))] = '3'
        if len(potentials[2] - potentials[1] - potentials[0]) == 0:
            self.known_nums[3] = set(potentials[2])
            self.known_strs[''.join(sorted(potentials[2]))] = '3'

    def get5(self):
        # diff of certain numbers are certain things (possibly with `and 3 in self.known_nums`)
        # (1 or 7) - 6 isn't in there
        for x in self.digits:
            if len(x) != 5:
                continue
            if set(x).isdisjoint((self.known_nums.get(1) or self.known_nums.get(7, set('abcdefg'))) - (self.known_nums.get(6) or set()))\
                    or (set(x).issubset(self.known_nums.get(9) or set()) and self.known_strs.get(x) != '3')\
                    or (len(set(x) - self.known_nums.get(4, set())) == 2 and self.known_strs.get(x) != '3'):
                self.known_nums[5] = set(x)
                self.known_strs[x] = '5'

    def get6(self):
        # if X - 1 or X - 7 isn't empty
        for x in self.digits:
            if len(x) != 6:
                continue
            if not set(x).issuperset(self.known_nums.get(1) or self.known_nums.get(7, set()))\
                    or set(x).issuperset(self.known_nums.get(5, set('z'))):
                self.known_nums[6] = set(x)
                self.known_strs[x] = '6'

    def get9(self):
        # 7 + 4 is subset
        for x in self.digits:
            if len(x) != 6:
                continue
            if set(x).issuperset(self.known_nums.get(4, set('z'))) or set(x).issuperset(self.known_nums.get(3, set('z'))):
                self.known_nums[9] = set(x)
                self.known_strs[x] = '9'


with open('day8.txt') as f:
    data = [ReadOut(line) for line in f.readlines()]
    # data = []
    # for line in f.readlines():
    #     out = list(map(lambda x: ''.join(sorted(x)), line.split(' | ')[1].split()))
    #     clues = set(line.strip().replace(' |', '').split())
    #     data.append(([{''.join(sorted(digit)): LENGTHS[len(digit)]} for digit in clues], out))

# data = [([{letters: possible nums, ...}, [output])], ...]
# data = list of tuples of (list of dicts, list of keys)

# after output: int(''.join([str(mapping[x]) for x in answers]))
print([f"{k} = {v}" for k, v in data[0].known_strs.items()])
print(sum([x.get_out_int() for x in data]))

# 0: 6 abcefg   X - 4 isn't empty
# 1: 2 cf       Given
# 2: 5 acdeg
# 3: 5 acdfg    1 or 7 is subset
# 4: 4 bcdf     Given
# 5: 5 abdfg
# 6: 6 abdefg   if X - 1 or X - 7 isn't empty
# 7: 3 acf      Given
# 8: 7 abcdefg  Given
# 9: 6 abcdfg   7 + 4 is subset

# a: 7 - 1
# b:
# c: 8 - 6
# d: 8 - 0
# e: 8 - 9 | 6 - 5
# f:
# g:

# could set up each digit as a dictionary to set(range(10))
# first drop based on number of digits
# then do random rules?
