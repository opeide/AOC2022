

if __name__ == '__main__':
    with open('day2_input.txt','r') as f:
        lines = f.readlines()
    lines = [l.strip().split() for l in lines]
    decoding = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3}
    decodedLines = [ (decoding[line[0]], decoding[line[1]]) for line in lines]
    winCombinations = [(1, 2), (2, 3), (3, 1)]
    score = 0
    for playerChoices in decodedLines:
        score += playerChoices[1]
        if playerChoices in winCombinations:
            score += 6
        if playerChoices[0] == playerChoices[1]:
            score += 3
    print(score)

    #bonus
    decodedLines = [ (decoding[line[0]], line[1]) for line in lines]
    opp2draw = [None, 1,2,3]
    opp2win = [None, 2,3,1]
    opp2lose = [None, 3,1,2]
    score = 0
    for opponent, strat in decodedLines:
        if strat == 'X': #lose
            choice = opp2lose[opponent]
        elif strat == 'Y': #draw
            choice = opp2draw[opponent]
            score += 3
        elif strat == 'Z': #win
            choice = opp2win[opponent]
            score += 6
        score += choice
    print(score)