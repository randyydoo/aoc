from icecream import ic
import sys



def solve(txt):
    with open(txt, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    print(len(lines))
    res = 0
    j = 0
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
        if bag['blue'] <= 14 and bag['green'] <= 13 and bag['red'] <= 12:
            res += int(l[1][:len(l[1])-1])
                        
    

    print(res)


solve('tst.txt')    
solve('inp.txt')
