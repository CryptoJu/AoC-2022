import numpy as np; import copy
from functools import reduce
with open('input/d9_input.txt','r') as f:
    pinput = f.readlines()
commands = []
for line in pinput:
    cmd, amount = line.strip('\n').split()
    commands.append((cmd, amount))

x = 300; y = 300; grid = [ ['.'] * x for _ in range(y)] # initialize griddddddddddddddddddddddddddddddddddddddddddddddddddd
visited = copy.deepcopy(grid); visited_int = 0
headpos = [0, 0]; tailpos = [0, 0]   # starting point y, x
ty = tailpos[0]; tx = tailpos[1]; hy = headpos[0]; hx = headpos[1]

for command in commands:  
    cmd = command[0]; amt = int(command[1])
    
    for i in range(amt):
        grid[hy][hx] = '.'
        grid[ty][tx] = '.'

        if cmd == 'R':
            hx += 1                     
        elif cmd == 'L':      
            hx -= 1                        
        elif cmd == 'U':
            hy -= 1
        elif cmd == 'D':
            hy += 1

        if hx == tx + 2:        # tail move right if head is 2 right
            tx += 1

            if hy == ty - 1:
                ty -= 1
            elif hy == ty + 1:
                ty += 1

        elif hx == tx - 2:              # go left if head is 2 left
            tx -= 1

            if hy == ty - 1:
                ty -= 1
            elif hy == ty + 1:
                ty += 1

        elif hy == ty + 2:          # go down if head is 2 down
            ty += 1

            if hx == tx + 1:
                tx += 1
            elif hx == tx -1:
                tx -= 1

        elif hy == ty - 2:          # go up if head is 2 up
            ty -= 1

            if(hx == tx + 1):
                tx += 1
            elif(hx == tx - 1):
                tx -= 1

        visited[ty][tx] = 'x'
        grid[hy][hx] = 'H'
        grid[ty][tx] = 'T'

for i in range(len(visited)):
    for j in range(len(visited[0])):
        if visited[i][j] == 'x':
            visited_int += 1
print(visited_int)