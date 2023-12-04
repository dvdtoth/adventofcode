file = open('input').read().splitlines()
total = 0
for line in file:
    win,draw = line.split(': ')[1].split('|')[0].split(), line.split(': ')[1].split('|')[1].split()
    points = 0
    for w in win:
        if w in draw:
            if points == 0:
                points = 1
            else:
                points = points * 2
    total += points
print(total)