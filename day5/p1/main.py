from collections import defaultdict
from icecream import ic
import sys


class Solution:
    def __init__(self, file):
        with open(file, 'r') as file:
            self.lines = [line.strip() for line in file.readlines()]

    def swap(self, temp_dic):
        new_dic = {}
        for k,v in temp_dic.items():
            new_dic[v] = v

        return new_dic

 
    def solve(self):
        temp = self.lines[0].split('seeds:')
        temp2 = temp[1].split(' ')
        valid = []
        dest_res = float('inf')

        for num in temp2:
            if num.isdigit():
                valid.append(int(num))
        for val in valid:
            d = {}
            curr = val
            for i, line in enumerate(self.lines):
                if 'map' in line and d:
                    curr = d[curr]
                    d = self.swap(d)
                    continue
                elif i == 0 or not line or ':' in line:
                    continue
                line = line.split(' ')
                dest, src, rnge = int(line[0]), int(line[1]), int(line[2])
                diff = dest - src
                if src <= curr < src+rnge:
                    d[curr] = curr + diff
                elif curr not in d:
                    d[curr] = curr
            dest_res = min(dest_res, d[curr])
        print(dest_res)
              

# test = Solution('tst.txt')
# test.solve()

inp = Solution('inp.txt')
inp.solve()
