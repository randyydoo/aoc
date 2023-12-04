from icecream import ic
import sys

def solve(text):
    with open(text, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    res = 0
    for j, line in enumerate(lines):
        game1, game2 = set(),set()
        line1 = line.split(' ')
        flag = False
        for i, num in enumerate(line1):
            num = num.strip()
            if num == '|':
                flag = True
                continue
            if i >= 2 and num.isdigit() and not flag:
                    game1.add(int(num)) 
            elif i >= 2 and num.isdigit() and flag and int(num) in game1:
                    game2.add(int(num))
        temp = 0
        for k in range(len(game2)):
            if k == 0:
                temp += 1
            else:
                temp *= 2
        res += temp
        ic(game1, game2)
    print(res)





# solve('tst.txt')
solve('inp.txt')
