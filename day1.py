
if __name__ == '__main__':
    with open('day1_input.txt','r') as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    elfWeights = [0]
    for l in lines:
        if l == '': #new elf
            elfWeights.append(0)
        else:
            elfWeights[-1] += int(l)
    print(max(elfWeights))
    #bonus
    print(sum(sorted(elfWeights)[-3:]))