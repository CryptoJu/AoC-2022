import re

with open('input/d5_input.txt','r') as f:
    pinput = f.readlines()

loesung_p1 = ''
loesung_p2 = ''
stacks = [
    ['N','T','B','S','Q','H','G','R'],
    ['J','Z','P','D','F','S','H'],
    ['V','H','Z'],
    ['H','G','F','J','Z','M'],
    ['R','S','M','L','D','C','Z','T'],
    ['J','Z','H','V','W','T','M'],
    ['Z','L','P','F','T'],
    ['S','W','V','Q'],
    ['C','N','D','T','M','L','H','W']
]

instructions = pinput[10:]

def p1():
    loesung_p1 = ''
    for inst in instructions:
        amount = int(re.search('move (.*) from', inst).group(1))
        phrom = int(re.search('from (.*) to', inst).group(1))
        to = int(re.search('to (.*)', inst).group(1))

        for i in range(0, amount, 1):   # phrom wird gepopt, to wird gepusht       
            element = stacks[phrom-1][0]
            stacks[phrom-1].pop(0)
            stacks[to-1].insert(0,element)
            
    for elem in stacks:
        loesung_p1 += str(elem[0])

    print(loesung_p1)

def p2():
    loesung_p2 = ''
    for inst in instructions:
        amount = int(re.search('move (.*) from', inst).group(1))
        phrom = int(re.search('from (.*) to', inst).group(1))
        to = int(re.search('to (.*)', inst).group(1))

        for i in range(0, amount, 1):   # phrom wird gepopt, to wird gepusht       
            element = stacks[phrom-1][0]
            stacks[phrom-1].pop(0)
            stacks[to-1].insert(i,element)

    for elem in stacks:
        loesung_p2 += str(elem[0])
    
    print(loesung_p2)

p2()
