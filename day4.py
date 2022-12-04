with open('input/d4_input.txt','r') as f:
    pinput = f.readlines()

def p1():
    ergebnis = 0
    for line in pinput:
        line = line.strip('\n')
        sections = line.split(',')
        sec1, sec2 = sections[0].split('-'), sections[1].split('-')
        sec1, sec2 = range(int(sec1[0]), int(sec1[1]) +1, 1)  , range(int(sec2[0]), int(sec2[1])+ 1, 1) 
        sec1, sec2 = set(sec1), set(sec2)

        if sec1.issubset(sec2) or sec2.issubset(sec1):
            ergebnis += 1

    print(ergebnis)

def p2():
    ergebnis = 0
    for line in pinput:
        line = line.strip('\n')
        sections = line.split(',')
        sec1, sec2 = sections[0].split('-'), sections[1].split('-')
        sec1, sec2 = range(int(sec1[0]), int(sec1[1]) +1, 1)  , range(int(sec2[0]), int(sec2[1])+ 1, 1) 

        if any(item in sec1 for item in sec2) or any(item in sec2 for item in sec1):
            ergebnis += 1

    print(ergebnis)

if __name__ == '__main__':
    print(f'Ergebnis Part 1: {p1()}\nErgebnis Part 2: {p2()}')