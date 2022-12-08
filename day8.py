import numpy as np
from functools import reduce
with open('input/d8_input.txt','r') as f:
    pinput = f.readlines()

trees = []

for line in pinput:
    line = line.strip('\n')
    arraylength = int(len(line))
    trees.append([element for element in line])


def p1():
    visible = 0
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            cur = int(trees[i][j])
            left = trees[i][:j]
            right = trees[i][j+1:]
            right = [int(x) for x in right]
            left = [int(x) for x in left]
            down, up = [], []

            for elem in trees[0:i]:
                up.append(int(elem[j]))
            for elem in trees[i+1:]:
                down.append(int(elem[j]))

            if up == [] or down == [] or right == [] or left == []: # edges
                visible += 1
                continue

            if max(left, default=cur) < cur or max(right, default=cur) < cur or max(up, default=cur) < cur or max(down, default=cur) < cur:
                visible +=1
    
    return(visible)


def p2():
    ergebnis = []
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            value = 0
            scenic = []
            
            cur = int(trees[i][j])
            left = trees[i][:j]
            right = trees[i][j+1:]
            right = [int(x) for x in right]
            left = [int(x) for x in left]
            down, up = [], []

            for elem in trees[0:i]:
                up.append(int(elem[j]))
            for elem in trees[i+1:]:
                down.append(int(elem[j]))

            #print(f'Current Element: {cur}')
            #print(np.matrix(trees))
            #print(f'up: {up} Left: {left} down: {down}, Right: {right}, , ')
            if up == [] or down == [] or right == [] or left == []:
                continue        # skip edgy edges

            if up != []:
                for elem in reversed(up):
                    if elem < cur:                
                        value += 1
                    elif elem >= cur:
                        value += 1
                        break
            else:
                value = 1
            scenic.append(value)
            value = 0

            if left != []:
                for elem in reversed(left):
                    if elem < cur:                
                        value += 1
                    elif elem >= cur:
                        value += 1
                        break
            else:
                value = 1
            scenic.append(value)
            value = 0

            if down != []:
                for elem in down:
                    if elem < cur:                
                        value += 1
                    elif elem >= cur:
                        value += 1
                        break
            else:
                value = 1
            scenic.append(value)
            value = 0

            if right != []:
                for elem in right:
                    if elem < cur:                
                        value += 1
                    elif elem >= cur:
                        value += 1
                        break
            else:
                value = 1
            scenic.append(value)
            value = 0
        
            ergebnis.append(reduce(lambda x, y: x*y, scenic))
    return(max(ergebnis))        
    
print(f'Ergebnis Part 1: {p1()}\nErgebnis Part 2: {p2()}')
            
            

        