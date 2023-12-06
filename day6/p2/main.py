from icecream import ic
import sys


def main(file):
    with open(file, 'r') as file:
        lines = [line.strip().split(':') for line in file.readlines()]
    
    time, dist = lines[0][1].strip(), lines[1][1].strip()
    time , dist = time.split(' '), dist.split(' ')
    t1, d1 = '', ''
    for t in time:
        if t.isdigit():
            t1 += t

    for d in dist:
        if d.isdigit():
            d1 += d
    t1, d1 = int(t1), int(d1)
    l, r = 1, t1-1
    l_f, r_f = False, False
    ic(t1, d1)
    while not l_f or not r_f:
        if l*(t1-l) > d1 and not l_f:
            l_f = True
        elif not l_f:
            l += 1
        if r*(t1-r) > d1 and not r_f:
            r_f = True
        elif not r_f:
            r -= 1
    ic(l, r)
    res = (r-l)+1
    print(res)

main('tst.txt')
# main('inp.txt')
