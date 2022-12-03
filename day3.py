import string
with open('input/d3_input.txt','r') as f:
    pinput = f.readlines()
zeichensystem = string.ascii_lowercase + string.ascii_uppercase

def p1():
    summe = 0
    for line in pinput:
        mid = int(len(line) / 2)
        line = [line[:mid], line[mid:].strip('\n')]
        for char in line[1]:
            if char in line[0]:
                summe += (zeichensystem.index(char) + 1)
                break
        return(summe)

def p2():  
    summe = 0; count = 1; group = []

    for line in pinput:
        if count == 3:
            group.append(line.strip('\n'))
            for char in group[2]:
                if char in group[0] and char in group[1]:
                    summe += (zeichensystem.index(char) + 1)
                    break
            group = []; count = 1; continue
        if count < 3:
            group.append(line.strip('\n'))
            count += 1
    return(summe)

if __name__ == '__main__':
    print(f'Ergebnis Part 1: {p1()}\nErgebnis Part 2: {p2()}')

    