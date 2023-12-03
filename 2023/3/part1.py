# turn into a 2 dim array
file = open('input').read().splitlines()
# turn . into 'a' so I can use isalnum() for symbols
lines = [list(line.replace('.','a')) for line in file]

# get dimensions of the doc
X = len(lines[0])
Y = len(lines)
total = 0

neighbors = lambda x,y: [(x2, y2) for x2 in range(x-1, x+2)
                           for y2 in range(y-1, y+2)
                           if (-1 < x < X and
                               -1 < y < Y and
                               (x != x2 or y != y2) and
                               (0 <= x2 < X) and
                               (0 <= y2 < Y))]

for i,l in enumerate(lines):
    current_digit = str()
    addit = False
    for j,c in enumerate(l):
        if c.isdigit():
            current_digit += c
            for n in neighbors(i,j):
                # There is a neighbour symbol
                if not lines[n[0]][n[1]].isalnum():
                    # print(c + ' has a neighbour symbol')
                    addit = True       
            if addit == True:
                if not (j+1 < len(l) and lines[i][j+1].isdigit()):
                    total += int(current_digit)
                    # print(current_digit + ' is a part number')
                    current_digit = str()
                    addit = False
        else: 
            current_digit = str()
            addit = False

print(total)