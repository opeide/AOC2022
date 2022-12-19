import numpy as np

with open('day14_input.txt','r') as f:
    lines = f.readlines()
#lines = [line.rstrip() for line in lines]
lines = [[[int(p.rstrip())for p in point.split(',')] for point in line.split('->')] for line in lines]
lines = np.asarray(lines)
grid = np.zeros((200,1000))
highestY = 0
highestX = 0
for line in lines:
    for i in range(len(line)-1):
        p1, p2 = line[i], line[i+1]
        rows = sorted([p1[1], p2[1]])
        cols = sorted([p1[0], p2[0]])
        grid[ rows[0]:rows[1]+1, cols[0]:cols[1]+1] = 1
        if rows[1] > highestY:
            highestY = rows[1]
        if cols[1] > highestX:
            highestX = cols[1]

print(highestY, highestX)
#bonus floor
grid[highestY+2, :] = 1

hasFallenOut = False
numSand = 0
while not hasFallenOut:
    pos = [0, 500]
    while True:
        if pos[0] >= grid.shape[0]-1:
            hasFallenOut = True
            print('sand fell out bottom')
            break
        elif pos[1] >= grid.shape[1]-1:
            raise Exception('sand fell out side')

        if not grid[pos[0]+1, pos[1]]: #down
            pos[0] += 1
        elif not grid[pos[0]+1, pos[1]-1]: #left diagonal
            pos[0] += 1
            pos[1] -= 1
        elif not grid[pos[0]+1, pos[1]+1]: #right diagonal
            pos[0] += 1
            pos[1] += 1
        else:
            if grid[pos[0], pos[1]] == 1:
                print('hole covered')
                hasFallenOut = True
                break
            grid[pos[0], pos[1]] = 1
            numSand += 1
            print(f'placed sand #{numSand}')
            break

print(f'num sand: {numSand}')