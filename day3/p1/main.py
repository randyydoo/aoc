from icecream import ic
import sys

def search(i, j, n, m, lines):
    for x,y in ((1,0), (0,1), (0,-1), (-1,0),(-1,1), (-1,-1), (1,1), (1,-1)):
        if 0 <= i+x < n and 0 <= j+y < m and lines[i+x][j+y] != '.' and not lines[i+x][j+y].isdigit():
            return True
    return False

def solve(text):
    with open(text, 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    n,m = len(lines), len(lines[0])
    valid = []
    res = 0
    for i,line in enumerate(lines):
        temp = ''
        indexes = []
        flag = False
        for j, c in enumerate(line):
            if c.isdigit():
                temp += c
                indexes.append((i,j))
                if search(i,j, n,m,lines):
                    flag = True
            if temp and flag and (not c.isdigit() or j == m-1):
                    print(temp, i, j)
                    res += int(temp)
                    valid.append(temp)
                
            if not c.isdigit():
                temp = ''
                indexes = []
                flag = False
    print(res)
# solve('tst.txt')
solve('inp.txt')
