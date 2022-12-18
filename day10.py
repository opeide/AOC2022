



with open('day10_input.txt','r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]

class SignalProcess:
    def __init__(self, targetCycles):
        self.targetCycles = targetCycles
        self.cycle = 1
        self.register = 1
        self.signalSum = 0
    
    def noop(self):
        self.cycle += 1
        self.check_cycle()
        self.draw()

    def addx(self, val):
        self.noop()

        self.cycle += 1
        self.draw()
        self.register += val
        self.check_cycle()

    def check_cycle(self):
        if self.cycle in self.targetCycles:
            #print(f'c{self.cycle} reg {self.register}')
            self.signalSum += self.register * (self.cycle)

    def draw(self):
        col = (self.cycle-2) % 40 
        if col == 0:
            print('\n')
        if abs(col-self.register) <=1:
            print('#', end='')
        else:
            print('.', end='')
        #print(f'(c{self.cycle}col{col}r{self.register})', end='')


cycle = 0
register = 1
targetCycles = [20, 60, 100, 140, 180, 220]
signalSum = 0
process = SignalProcess(targetCycles)
for line in lines:
    #print(line)
    if line == 'noop':
        process.noop()
    elif 'addx' in line:
        val = int(line.split(' ')[1])
        process.addx(val)
    #input()

print('')
print(process.signalSum)