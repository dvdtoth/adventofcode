file = open('input').read().splitlines()

# recurse to the bottom
def process(tl):
    nl =[]
    for n in range(len(tl)-1):
        nl.append(tl[n+1]-tl[n])

    if all(l == 0 for l in nl):
        return tl[0]
    else:
        return tl[0] - process(nl)

total = 0
for l in file:
    tl = [int(n) for n in l.split()]
    total += process(tl)
print(total)