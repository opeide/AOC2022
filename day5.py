
from copy import deepcopy


with open('day5_input.txt','r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]

#parse container stacks
stacks = [[] for _ in range(9)]
for line in reversed(lines[:8]):
    line = line.replace(' '*4, '[-] ')
    line = line.split('[')[1:]
    line = [x[0] for x in line]
    for col, letter in enumerate(line):
        letter = letter
        if letter.isalnum():
            stacks[col].append(letter)


initialStacks = deepcopy(stacks)

for line in lines[10:]:
    num, src, dst = line.replace('move ', '').replace(' from ',',').replace(' to ', ',').split(',')
    num, src, dst = int(num), int(src)-1, int(dst)-1
    for i in range(num):
        stacks[dst].append(stacks[src].pop(-1))

ans = ''
for stack in stacks:
    ans += stack[-1]
print(ans)


#bonus
stacks = initialStacks
for line in lines[10:]:
    num, src, dst = line.replace('move ', '').replace(' from ',',').replace(' to ', ',').split(',')
    num, src, dst = int(num), int(src)-1, int(dst)-1
    crates = stacks[src][-num:]
    del stacks[src][-num:]
    stacks[dst].extend(crates)        

ans = ''
for stack in stacks:
    ans += stack[-1]
print(ans)
