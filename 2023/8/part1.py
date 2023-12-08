file = open('input').read().splitlines()
direction = file[0].replace('L', '0').replace('R', '1')

move = {}
for l in file[2::]:
    move[l[:3]] = (l.split('(')[1][:3], l.split(')')[0][-3:])

s = 0
loc = 'AAA'
while loc != 'ZZZ':
    loc = move[loc][int(direction[s % len(direction)])]
    s += 1
print(s)