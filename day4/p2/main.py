from icecream import ic
import re
import sys
from collections import defaultdict

def solve(text):
    with open(text, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    res = 0
    copies = defaultdict(int)
    valids = defaultdict(list)
    for line in lines:
        valid, game2 = set(),set()
        line = re.sub(r"\s+", " ", line)
        line1 = line.split(' ')
        game = int(line1[1][:len(line1[1])-1])
        copies[game] += 1
        flag = False
        for i, num in enumerate(line1):
            num = num.strip()
            if num == '|':
                flag = True
                continue
            if i >= 2 and num.isdigit() and not flag:
                    valid.add(int(num)) 
            elif i >= 2 and num.isdigit() and flag and int(num) in valid:
                    game2.add(int(num))

        for j in range(game+1, (game+1)+len(game2)):
            valids[game].append(j)
        # ic(valids[game], copies[game])
        for k in range(copies[game]):
            for valid in valids[game]:
                copies[valid] += 1
        # ic(copies)
    for vals in copies.values():
        res += vals
    print(res)





# solve('tst.txt')
solve('inp.txt')
