import numpy as np
from enum import Enum


with open('day13_input.txt','r') as f:
    lines = f.read()
lines = lines.split('\n\n')

def isList(arg):
    return '[' in arg

def toElements(arrString):
    if arrString[0] == '[':
        arrString = arrString[1:-1]
    if not arrString:
        print('empty')
        return []
    commaIdxs = []
    level = 0
    for i, letter in enumerate(arrString):
        level += int(letter == '[')
        level -= int(letter == ']')
        if level == 0 and letter ==',':
            commaIdxs.append(i)

    elements = [arrString[i+1:j] for i,j in zip([-1]+commaIdxs, commaIdxs+[len(arrString)])]
    print('commas ', commaIdxs, 'elements ', elements)
    return elements

class Validity(Enum):
    FALSE = 0
    TRUE = 1
    EQUALS = 2

def compare(left, right):
    print(f'comparing {left, right}')
    if isList(left) and isList(right):
        print('list v list')
        leftEls = toElements(left)
        rightEls = toElements(right)
        for i,lel in enumerate(leftEls):
            if i >= len(rightEls):
                print('right ran out')
                return Validity.FALSE    
            print(f'elements {lel}  ,  {rightEls[i]}')
            if compare(lel, rightEls[i]) == Validity.TRUE:
                print('left smaller')
                return Validity.TRUE
            elif compare(lel, rightEls[i]) == Validity.FALSE:
                print('right bigger')
                return Validity.FALSE
            elif compare(lel, rightEls[i]) == Validity.EQUALS:
                print('element equal')
                continue
        if len(leftEls) < len(rightEls):
            print('left ran out')
            return Validity.TRUE
        print('both lists equal')
        return Validity.EQUALS

    elif not isList(left) and not isList(right):
        print('int v int')
        if int(left) < int(right):
            return Validity.TRUE
        elif int(left) > int(right):
            return Validity.FALSE
        elif int(left) == int(right):
            return Validity.EQUALS

    else:
        if not isList(left):
            return compare(f'[{left}]', right)
        else:
            return compare(left, f'[{right}]')


correctIdxs = []
for i, line in enumerate(lines):
    left, right = line.split('\n')
    print(left)
    print(right)
    isValid = compare(left, right)
    print(isValid)
    if isValid == Validity.TRUE:
        correctIdxs.append(i+1)
    print('------'*4)

print(correctIdxs)
print(sum(correctIdxs))


#bonus
with open('day13_input.txt','r') as f:
    lines = f.readlines()
lines = [line.rstrip() for line in lines]
lines = [line for line in lines if line]
divider_packets = ['[[2]]', '[[6]]']
lines.extend(divider_packets)

print(lines)

sortedLines = []
for line in lines:
    idx = 0
    for i, sortedLine in enumerate(sortedLines):
        if compare(line, sortedLine) == Validity.TRUE:
            break
        idx += 1    
    sortedLines.insert(idx, line)

divider_packets_idxs = []
for i, line in enumerate(sortedLines):
    print(line)
    if line in divider_packets:
        divider_packets_idxs.append(i+1)
print('decoder key ', divider_packets_idxs[0]*divider_packets_idxs[1])