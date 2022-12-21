with open('input/d20_input.txt', 'r') as f:
    data = f.readlines()

nums = []; orignums = []
for elem in data:
    elem = elem.strip('\n'); elem = int(elem); nums.append(elem);  orignums.append(elem)

#print(f'Initial D: {nums}')


# find duplicate items using set()
seen = set()
duplicate_item = [x for x in nums if x in seen or (seen.add(x) or False)]

# printing duplicate elements
print('Duplicate Elements:', duplicate_item)