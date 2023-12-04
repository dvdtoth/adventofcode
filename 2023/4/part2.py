file = open('input').read().splitlines()
total = 0
counter = [1] * len(file)
for i, line in enumerate(file):
    win,draw = line.split(': ')[1].split('|')[0].split(), line.split(': ')[1].split('|')[1].split()
    matches = 0
    # this is a bruteforce solution, slow but it works
    # for the number of the copies of this card
    for c in range(counter[i]):
        # for each number in the win list
        for w in win:            
            if w in draw:
                matches += 1
        if matches > 0:
            for j in range(matches):
                if i+j <= len(counter):
                    counter[i+j+1] += 1
            matches = 0

print(sum(counter))