import numpy as np
from functools import reduce
with open('input/d9_input.txt','r') as f:
    pinput = f.readlines()
commands = []
for line in pinput:
    cmd, amount = line.strip('\n').split()
    commands.append((cmd, amount))

x = 6; y = 5; grid = [ ['.'] * x for _ in range(y)] # initialize gridddd
headpos = [4, 0]; tailpos = [4, 0]   # starting point y, x
ty = tailpos[0]; tx = tailpos[1]; hy = headpos[0]; hx = headpos[1]
print(np.matrix(grid))

for command in commands:  
    cmd = command[0]; amt = int(command[1])
    
    print(cmd, amt)

    for i in range(amt):
        grid[hy][hx] = '.'
        grid[ty][tx] = '.'

        if cmd == 'R':
            if hy != ty:
                if hx == tx + 1 and hy == ty - 1: # upper right
                    print('Soos')
            elif hx >= tx + 1:    
                hx += 1         
                tx += 1         
            else:
                hx += 1       
        elif cmd == 'L':
            if hy == ty - 1 and hx == tx -1:
                ty -= 1
                            # ab hier ist im Arsch
            if hx >= tx + 1:        
                hx -= 1             
                tx -= 1            
            else:
                hx -= 1

        elif cmd == 'U':
            if hx == tx + 1 and hy == ty - 1:   # upper right
                tx += 1
            elif hx == tx -1 and hy == ty - 1:
                tx -= 1
            if hy <= ty - 1:       # if head is more than 1 step above tail
                hy -= 1            # move head one up
                ty -= 1            # move tail one up
            else:
                hy -= 1
            
        elif cmd == 'D':
            if hy >= ty + 1:
                hy += 1
                ty += 1
            else:
                hy += 1
        #else: #head is on another ebene as tail
            #if hx == tx + 1 and hy == ty - 1: # upper right
                #tx += 1
                #print('ur')
            #elif hx == tx -1 and hy == ty - 1: # upper left
                #tx -= 1
                #print('ul')
            #elif hx == tx - 1 and hy == ty + 1:
                #print('dl')
            
                


        
        grid[hy][hx] = 'H'
        grid[ty][tx] = 'T'


        print(np.matrix(grid))
