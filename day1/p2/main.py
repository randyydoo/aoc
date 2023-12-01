import sys 

vals = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
digs = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

with open('inp2.txt', 'r') as file:
    lst = [line.strip() for line in file.readlines()]

res = 0
for line in lst:
    pos = {}
    for val in vals:
        start = 0
        while line.find(val, start) != -1:
            first = line.find(val, start) 
            pos[first] = vals[val]
            start = first + len(val)
        
        for i in range(len(line)):
            if line[i].isdigit():
                pos[i] = line[i]

    idx = sorted(pos)
    res += int(pos[idx[0]]+pos[idx[-1]])

print(res)
