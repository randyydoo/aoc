from icecream import ic
import sys
import numpy

def search(i, j, n, m, lines):
    nums = []
    visited = set()
    for x,y in ((1,0), (0,1), (0,-1), (-1,0),(-1,1), (-1,-1), (1,1), (1,-1)):
        if 0 <= i+x < n and 0 <= j+y < m and (i+x, j+y) not in visited and lines[i+x][j+y].isdigit():
            visited.add((i+x, j+y))
            c_row = i+x
            l, r = j+y, j+y
            while l >= 0 or r < m:
                if (r >= m and not lines[c_row][l].isdigit()) or (l < 0 and not lines[c_row][r].isdigit()) or (not lines[c_row][l].isdigit() and not lines[c_row][r].isdigit()):
                    break
                if l >= 0 and lines[c_row][l].isdigit():
                    visited.add((i+x, l))
                    l -= 1
                if r < m and lines[c_row][r].isdigit():
                    visited.add((i+x, r))
                    # ic(r)
                    # ic(m)
                    r += 1
            num = lines[c_row][l+1:r]
            nums.append(int(num))
    # ic(i, j,nums)
    return nums

def solve(text):
    with open(text, 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    n,m = len(lines), len(lines[0])
    valid = []
    res = 0
    for i,line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '*':
                adj = search(i, j, n, m, lines)
                if len(adj) == 2:
                    res += adj[0] * adj[1]
    print(res)
# solve('tst.txt')
solve('inp.txt')
