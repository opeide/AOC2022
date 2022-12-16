import string
import numpy as np



with open('day3_input.txt','r') as f:
    lines = f.readlines()
lines = [l.strip() for l in lines]

letters = string.ascii_lowercase + string.ascii_uppercase
priorityDict = {letter : i+1 for i,letter in enumerate(letters)}
prioritySum = 0
for sack in lines:
    comp1 = set(sack[:len(sack)//2])
    comp2 = set(sack[len(sack)//2:])
    errorType = comp1.intersection(comp2).pop()
    prioritySum += priorityDict[errorType]
print(prioritySum)

#bonus
prioritySum = 0
for sack1, sack2, sack3 in np.array(lines).reshape((-1,3)):
    common = set(sack1).intersection(sack2).intersection(sack3).pop()
    prioritySum += priorityDict[common]
print(prioritySum)