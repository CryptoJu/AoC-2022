with open('input/d6_input.txt','r') as f:
    pinput = f.readlines()

def d1():
    for line in pinput:
        line = line.strip('\n')
        for i in range(4, len(line), 1):
            if line[i] != line[i-1] and line[i] != line[i-2] and line[i] != line[i-3] and line[i-1] != line[i-2] and line[i-1] != line[i-3] and line[i-2] != line[i-3] and line[i-1] != line[i-2]:
                print(f'Das Ergebnis für Teil 1 ist: {i+1}')
                break


def d2():
    counter = 0
    for line in pinput:
        line = line.strip('\n')
        for i in range(14, len(line), 1):        
            checker = ''.join(dict.fromkeys(line[counter:i]))  
            if checker == line[counter:i]:
                print(f'Das Ergebnis für Teil 2 ist: {i}')
                break
            counter += 1
    

d1();d2()
