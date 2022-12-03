with open('input/d1_input.txt','r') as f:
    pinput = f.readlines()

calorieCount = 0
list = []

for line in pinput:
    line = line.strip('\n')
    if line != '':
        calorieCount += int(line)
    else:
        list.append(calorieCount)
        calorieCount = 0
list2 = sorted(list, reverse=True)
print(f'Ergebnis: {max(list)}\nErgebnis2: {list2[0]+list2[1]+list2[2]}')

