from math import lcm

file = open('input').read().splitlines()
direction = file[0].replace('L', '0').replace('R', '1')

move = {}
for l in file[2::]:
    move[l[:3]] = (l.split('(')[1][:3], l.split(')')[0][-3:])

locs = [key for key in move if key.endswith('A')]
paths = []
for l in locs:
    s = 0
    cn = l
    while not cn.endswith('Z'):
        cn = move[cn][int(direction[s % len(direction)])]
        s += 1
    paths.append(s)

print(lcm(*paths))