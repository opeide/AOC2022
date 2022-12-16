



with open('day4_input.txt','r') as f:
    lines = f.readlines()
lines = [l.strip() for l in lines]

pairs = [line.split(',') for line in lines]
pairs = [[list(map(int, ass.split('-'))) for ass in p] for p in pairs]

numFullyContains = 0
for ass1, ass2 in pairs:
    if ass1[0] <= ass2[0] and ass1[1] >= ass2[1]:
        numFullyContains += 1
    elif ass2[0] <= ass1[0] and ass2[1] >= ass1[1]:
        numFullyContains += 1
print(numFullyContains)

#bonus
numOverlap = 0
for ass1, ass2 in pairs:
    if ass1[0] <= ass2[0] <= ass1[1]:
        numOverlap += 1
    elif ass2[0] <= ass1[0] <= ass2[1]:
        numOverlap += 1
print(numOverlap)