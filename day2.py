def p1():
    with open('input/d2_input.txt','r') as f:
        pinput = f.readlines()

    score = 0
    for line in pinput:
        line = line.strip('\n').split(" ")
        enemy, you = line[0], line[1]

        if you == 'X' and enemy == 'A': # rock vs rock
            score += 4
        if you == 'X' and enemy == 'B': # rock vs paper
            score += 1
        if you == 'X' and enemy == 'C': # rock vs scissors
            score += 7
        if you == 'Y' and enemy == 'A': # paper vs rock
            score += 8
        if you == 'Y' and enemy == 'B': # paper vs paper
            score += 5
        if you == 'Y' and enemy == 'C': # paper vs scissor
            score += 2
        if you == 'Z' and enemy == 'A': # scissor vs rock
            score += 3
        if you == 'Z' and enemy == 'B': # scissor vs paper
            score += 9
        if you == 'Z' and enemy == 'C': # scissor vs scissor
            score += 6


    print(score)

def p2():
    with open('d2_input.txt','r') as f:
        pinput = f.readlines()

    score = 0
    for line in pinput:
        line = line.strip('\n').split(" ")
        enemy, round = line[0], line[1]

        if round == 'X' and enemy == 'A': # lose, enemy rock, take scissors
            score += 3
        if round == 'X' and enemy == 'B': # lose, enemy paper, take rock
            score += 1
        if round == 'X' and enemy == 'C': # lose, enemy scissors, take paper
            score += 2
        if round == 'Y' and enemy == 'A': # draw, enemy rock, take rock
            score += 4
        if round == 'Y' and enemy == 'B': # draw, enemy paper, take paper
            score += 5
        if round == 'Y' and enemy == 'C': # draw, enemy scissors, take scissors
            score += 6
        if round == 'Z' and enemy == 'A': # win, enemy rock, take paper
            score += 8
        if round == 'Z' and enemy == 'B': # win, enemy paper, take scissors
            score += 9
        if round == 'Z' and enemy == 'C': # win, enemy scissors, take rock
            score += 7


    print(score)