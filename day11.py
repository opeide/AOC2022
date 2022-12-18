import numpy as np


class Monkey:
    def __init__(self, items, operation, test, iftrue, iffalse):
        self.items = items
        self.operation = operation
        self.test = test
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.totalInspections = 0

with open('day11_input.txt','r') as f:
    lines = f.read()
monkeytext = lines.split('\n\n')

monkeys = []
for i, text in enumerate(monkeytext):
    lines = text.split('\n')  
    _, items, operation, test, iftrue, iffalse = lines
    
    items = [int(i.replace(',','')) for i in items.split(' ')[4:]]
    
    if '*' in operation:
        val = operation.split('*')[1].strip()
        if val == 'old':
            operation = lambda x: x**2
        else:
            operation = lambda x,v=int(val): x*v
    elif '+' in operation:
        val = int(operation.split('+')[1].strip())
        operation = lambda x,v=val: x+v
    
    testval = int(test.split(' ')[-1])
    test = lambda x,v=testval: x%v == 0

    iftrue = int(iftrue[-1])
    
    iffalse = int(iffalse[-1])
    monkeys.append(Monkey(items, operation, test, iftrue, iffalse))


for round in range(1,10001):
    for monkey in monkeys:
        for worry in monkey.items:
            worry = monkey.operation(worry)
            #worry = worry // 3
            worry = worry % (11*5*19*13*7*17*2*3)

            if monkey.test(worry):
                monkeys[monkey.iftrue].items.append(worry)
            else:
                monkeys[monkey.iffalse].items.append(worry)
        numInspections = len(monkey.items)
        monkey.totalInspections += numInspections
        monkey.items = []
    if round in [1, 20, 1000, 2000, 5000, 10000]:
        print(f'\nround {round}')
        for monkey in monkeys:
            print(monkey.totalInspections)

for monkey in monkeys:
    print(monkey.totalInspections)
topinspections = sorted([m.totalInspections for m in monkeys])[-2:]
print('top2prod', topinspections[0]*topinspections[1])

#bonus

