from icecream import ic
import sys


def main(file):
    with open(file, 'r') as file:
        lines = [line.strip().split(':') for line in file.readlines()]
    
    time, dist = lines[0][1].strip(), lines[1][1].strip()
    time , dist = time.split(' '), dist.split(' ')
    times, dists = [], []
    for t in time:
        if t.isdigit():
            times.append(int(t))

    for d in dist:
        if d.isdigit():
            dists.append(int(d))
    res = 1
    for i in range(4):
        t1, d1 = times[i], dists[i]
        l, r = 1, t1-1
        l_f, r_f = False, False
        while not l_f or not r_f:
            if l*(t1-l) > d1 and not l_f:
                l_f = True
            elif not l_f:
                l += 1
            if r*(t1-r) > d1 and not r_f:
                r_f = True
            elif not r_f:
                r -= 1
        res *= (r-l)+1
    print(res)

main('tst.txt')
# main('inp.txt')
