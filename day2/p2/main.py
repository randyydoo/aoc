from icecream import ic
import sys


def solve(txt):
    with open(txt, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    res = 0
    vals = []
    for line in lines:
        bag = {'blue': 0, 'red': 0, 'green': 0}
        # ic(line, j)
        l = line.split(' ')
        split = l[2:]
        for i in range(0,len(split), 2):
            ct = int(split[i])
            if 'blue' in split[i+1]:
                bag['blue'] = max(ct, bag['blue'])
            elif 'green' in split[i+1]:
                bag['green'] = max(ct, bag['green'])
            else:
                bag['red'] = max(ct, bag['red'])

        b_ct, r_ct, g_ct = bag['blue'], bag['red'], bag['green']
        temp = 1
        if not b_ct and not r_ct and not g_ct:
            continue
        else:
            for cts in bag.values():
                if cts > 0:
                    temp *= cts
        vals.append(temp)
                        
    for val in vals: 
        res += val
    print(res)


solve('tst.txt')    
solve('inp.txt')
