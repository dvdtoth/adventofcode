file = open('input').read().splitlines()
seeds = list(map(int, file[0].split(':')[1].split()))
# dest src range
maps = [list(map(int, seeds))]
m = 0
for line in file[1:]:
    if 'map' in line:
        if m > 0: seeds = maps[m]+seeds
        m += 1
        maps.append([])
    if len(line) > 0 and line[0].isdigit(): 
        l = list(map(int, line.split()))
        sc = seeds.copy()
        for s in sc:
            if l[1] <= s <= (l[1]+l[2]):
                maps[m].append(l[0]+s-l[1])
                seeds.remove(s)
print('result:', min(seeds + maps[-1]))