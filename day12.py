import numpy as np
import string

#use policy iteration to find optimal global policy map

letter2num = {letter : i for i,letter in enumerate(string.ascii_lowercase+'E'+'S')}
startVal = letter2num['S']
endVal = letter2num['E']

with open('day12_input.txt','r') as f:
    lines = f.read()
lines = lines.split('\n')
heightMap = np.array([[letter2num[letter] for letter in line] for line in lines])
heightMap[heightMap == startVal] = letter2num['a']
startVal = letter2num['a']

distanceMap = np.full_like(heightMap, 99999)
policyMap = np.full_like(heightMap, None, dtype=object)
distanceMap[heightMap == endVal] = 0

def within_bounds(row, col):
    rowOk = 0 <= row < heightMap.shape[0]
    colOk = 0 <= col < heightMap.shape[1]
    ok = np.all(rowOk and colOk)
    return ok


for i in range(1000):
    print(f'iteration {i}')
    newDistanceMap = distanceMap.copy()
    for row in range(heightMap.shape[0]):
        for col in range(heightMap.shape[1]):
            #print(f'rowcol {row, col}, shape {heightMap.shape}')
            for vec in [[1,0], [-1,0], [0,1], [0,-1]]:
                if not within_bounds(row+vec[0], col+vec[1]): continue
                height = heightMap[row, col]
                targetHeight = heightMap[row+vec[0], col+vec[1]] 
                isReachable = np.all(targetHeight-height<=1)
                if not isReachable: continue
                dist = 1 + distanceMap[row+vec[0], col+vec[1]]
                if dist < distanceMap[row, col]:
                    print('updating policy')
                    newDistanceMap[row, col] = dist
                    policyMap[row, col] = vec
    if np.all(newDistanceMap == distanceMap):
        print('converged')
        break
    distanceMap = newDistanceMap

distList = []
for pos in np.argwhere(heightMap == startVal):
    dist = distanceMap[pos[0], pos[1]]
    print(f'start pos: {pos}, dist:{dist}')
    distList.append(dist)
print(f'min dist: {min(distList)}')