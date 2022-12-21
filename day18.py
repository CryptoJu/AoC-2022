with open('input/d18_input.txt', 'r') as f:
    data = f.readlines()

sides = 6 * len(data)
cubes = []
for cube in data:
    cube = cube.strip('\n')
    x, y, z = int(cube.split(',')[0]), int(cube.split(',')[1]), int(cube.split(',')[2])
    cubes.append([x,y,z])

for cube in cubes:
    if [cube[0]+1, cube[1], cube[2]] in cubes:
        sides -= 1
    if [cube[0]-1, cube[1], cube[2]] in cubes:
        sides -= 1
    if [cube[0], cube[1]+1, cube[2]] in cubes:
        sides -= 1
    if [cube[0], cube[1]-1, cube[2]] in cubes:
        sides -= 1
    if [cube[0], cube[1], cube[2]+1] in cubes:
        sides -= 1
    if [cube[0], cube[1], cube[2]-1] in cubes:
        sides -= 1

print(f'Das Ergebnis für Part 1: {sides}')