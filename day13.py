import ast
with open('input/d13_input.txt', 'r') as f:
    data = f.read().split('\n\n')


for line in data:
    left = line.split('\n')[0]; right = line.split('\n')[1]

    print(left, right)
    for i in range(len(line)):
        if line[i] == '[':
            pass