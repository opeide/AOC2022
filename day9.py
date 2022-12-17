import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

with open('day9_input.txt','r') as f:
    lines = f.readlines()
lines = [l.rstrip().split() for l in lines]

dir2xy = {'R':np.array([1,0]), 'U':np.array([0,1]), 'L':np.array([-1,0]), 'D':np.array([0,-1])}

head = np.array([0,0])
tail = np.array([0,0])
tailHistory = [tuple(tail)]
for direction, steps in lines:
    vec = dir2xy[direction]
    for _ in range(int(steps)):
        if np.linalg.norm(head+vec-tail)>1.5: #head pulling tail
            if np.all(head!=tail): #diagonal
                tail = head.copy()
                head += vec
            else:
                head += vec
                tail += vec
            tailHistory.append(tuple(tail))
        else:
            head += vec
print(len(set(tailHistory)))

#bonus
class Rope:
    def __init__(self, numKnots):
        self.tail = None
        if numKnots-1>0:
            self.tail = Rope(numKnots-1)
        self.xy = np.array([20,20])
        self.history = [tuple(self.xy)]

    def get_final_tail(self):
        if self.tail is None:
            return self
        return self.tail.get_final_tail() 

    def move(self, vec):
        vec = vec.astype(int)
        if self.tail is None: 
            self.xy += vec
        else:
            if np.linalg.norm(self.xy+vec-self.tail.xy)>np.sqrt(2): #pulling tail
                if np.all(vec != 0): #diagonal vector
                    if np.all(self.xy != self.tail.xy): #start diagonally
                        vecTail = (vec+self.xy-self.tail.xy)//2
                        self.xy += vec
                        self.tail.move(vecTail)
                    else: 
                        self.xy += vec
                        self.tail.move(vec)
                elif np.all(self.xy != self.tail.xy): #straight vec, but start diagonally
                    vecTail = self.xy - self.tail.xy
                    self.xy += vec
                    self.tail.move(vecTail)
                else: #simple straight movement
                    self.xy += vec
                    self.tail.move(vec)
            else:
                self.xy += vec
        self.history.append(tuple(self.xy))

    def show_whole_rope(self):
        img = np.zeros((50,50))
        img[20,20]=1
        rope = self
        for i in range(3,99):
            xy = rope.xy
            img[xy[0], xy[1]] = i
            rope = rope.tail
            if rope is None:
                break
        img = np.rot90(img)
        cmap = plt.get_cmap('tab20', lut=15)
        img = cmap(img.astype(int))
        Image.fromarray((img[:,:,:3]*255).astype(np.uint8)).resize((1000,1000), Image.NEAREST).show()
    
    def show_history(self):
        img = np.zeros((50,50))
        for xy in self.history:
            img[xy[0], xy[1]] = 1
        img = np.rot90(img)
        Image.fromarray(img*255).resize((1000,1000), Image.NEAREST).show()

rope = Rope(10)
for direction, steps in lines:
    vec = dir2xy[direction]
    for _ in range(int(steps)):
        rope.move(vec)

    #rope.show_whole_rope()
    #input()
#rope.get_final_tail().show_history()
print(len(set(rope.get_final_tail().history)))