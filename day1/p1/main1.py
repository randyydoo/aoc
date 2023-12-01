import sys

with open('inp.txt', 'r') as file:
    lst = [line.strip() for line in file.readlines()]

nums = []

for line in lst:
    for i in range(len(line)):
        if line[i].isdigit():
            l = line[i]
            break
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            r = line[i]
            break
    nums.append(l+r)

res = 0
for num in nums:
    res += int(num)
print(res)

        


    
