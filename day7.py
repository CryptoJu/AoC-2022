with open('input/d7_input.txt','r') as f:
    pinput = f.read().split('\n$ ')[1:] # strip by newline and $ to get commands with outputs

path = []
folders = []
for elem in pinput:
    lines = elem.split('\n')

    cmd = lines[0]
    output = lines[1:]

    if 'cd' in cmd: #cd command
        _, directory = cmd.split()

        if directory == '..':
            path.pop()
        else:
            path.append(f'/{directory}')
    elif 'ls' in cmd:
        # dict aus current dir und subdirs und files
            childdirs = []
            files = []
            for o in output:
                if o.startswith('dir'):
                    childdirs.append(o.split()[1])
                else:
                    files.append((o.split()[0] , o.split()[1]))
            dic = { "name": f''.join(path), "childdirs": childdirs, "files": files}
            folders.append(dic)


def count_value(dict):
    total_folder_size = 0
    for file in dict['files']:
        size = int(file[0])
        total_folder_size += size
    return total_folder_size

def traverse(dict):
    total = 0
    childdirs = dict['childdirs']
    name = dict['name']
    total += count_value(dict)

    for child_name in childdirs: # a, d
        dict = [element for element in folders if element['name'] == f'{name}/{child_name}'][0]
        total += traverse(dict)
    
    return total

total_sizes = []
for elem in folders:
    if traverse(elem) <= 100000:
        total_sizes.append(traverse(elem))

print(f'Ergebnis Part 1: {sum(total_sizes)}')