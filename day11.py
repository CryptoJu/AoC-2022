import math
with open('input/d11_input.txt') as f:
    data = f.read().split('\n\n')

items = []
inspected = [0 for i in range(4)]

for monkeyblock in data:
    items.append([eval(i) for i in monkeyblock.split(': ')[1].strip("\n Operation'").split(', ')])

print(items)

    
for i in range(len(items)): # do it for five rounds
    operation, amt = data[i].split('Operation: new = old ')[1].split(' ')[0], data[i].split('Operation: new = old ')[1].split(' ')[1].strip('\n')
    test = data[i].split('divisible by ')[1].split('\n')[0]
    iftrue = data[i].split('If true: throw to monkey ')[1].split('\n')[0]
    iffalse = data[i].split('If false: throw to monkey ')[1]

    print(operation, amt)
    print(test)
    print(iftrue, iffalse)
    for j in range(len(items[i])): # for every element in list
        inspected[i] += 1
        old = items[i][j] // 3

        if amt == 'old':
            new = eval(f'{old} {operation} {old}')
        else:
            new = eval(f'{old} {operation} {amt}')
        if new % int(test) == 0:
            items[int(iftrue)].append(new)
        else:
            items[int(iffalse)].append(new)
            
    print(items)
print(inspected)
