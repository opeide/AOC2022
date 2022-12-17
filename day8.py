import numpy as np

with open('day8_input.txt','r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]
lines = [[int(el) for el in line] for line in lines]

trees = np.array(lines)
visible = np.zeros_like(lines)
for row in range(trees.shape[0]):
    for col in range(trees.shape[1]):
        visible[row, col] += np.all(trees[row, col] > trees[:row, col]) or np.all(trees[row, col] > trees[row+1:, col])
        visible[row, col] += np.all(trees[row, col] > trees[row, :col]) or np.all(trees[row, col] > trees[row, col+1:])
print(np.count_nonzero(visible))

#bonus
trees = np.array(lines)
numRows = trees.shape[0]
numCols = trees.shape[1]
maxProd = 0
for row in range(numRows):
    for col in range(numCols):
        if row < 2:
            continue
        #top
        top = 0
        for r in range(row-1, -1, -1):
            top += 1
            if trees[r, col] >= trees[row,col]: break
        #bottom
        bottom = 0
        for r in range(row+1, numRows):
            bottom += 1
            if trees[r, col] >= trees[row,col]: break
        #left
        left = 0
        for c in range(col-1, -1, -1):
            left += 1
            if trees[row, c] >= trees[row,col]: break
        #right
        right = 0
        for c in range(col+1, numCols):
            right += 1
            if trees[row, c] >= trees[row,col]: break
        prod = top*bottom*left*right
        if prod > maxProd:
            maxProd = prod
print(maxProd)