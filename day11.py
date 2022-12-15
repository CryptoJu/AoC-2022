with open('input/d11_input.txt') as f:
    data = f.read().split('\n\n')

items = []
monkeys = 8

inspected = [0 for i in range(monkeys)]

for monkeyblock in data:
    items.append([eval(i) for i in monkeyblock.split(': ')[1].strip("\n Operation'").split(', ')])

for rounds in range(20):
    for i in range(len(items)): # one round
        operation, amt = data[i].split('Operation: new = old ')[1].split(' ')[0], data[i].split('Operation: new = old ')[1].split(' ')[1].strip('\n')
        test = data[i].split('divisible by ')[1].split('\n')[0]
        iftrue = data[i].split('If true: throw to monkey ')[1].split('\n')[0]
        iffalse = data[i].split('If false: throw to monkey ')[1]

        for j in range(len(items[i])): # for every element in list
            inspected[i] += 1
            old = items[i][0]
            if amt == 'old':             
                new = eval(f'{old} {operation} {old}')
                new = new // 3
            else:
                new = eval(f'{old} {operation} {int(amt)}')
                new = new // 3
            
                
            if new % int(test) == 0:
                items[int(iftrue)].append(new)
                items[i].pop(0)
            else:
                items[int(iffalse)].append(new)
                items[i].pop(0)
                   
inspected_max = sorted(inspected, key=int, reverse=True)
print(f'Ergebnis Part 1: {inspected_max[0] * inspected_max[1]}')

