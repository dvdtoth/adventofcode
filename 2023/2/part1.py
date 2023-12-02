
# read file line by line
with open('input') as f:
    lines = f.readlines()

    # rule
    max_reds = 12
    max_greens = 13
    max_blues = 14

    total = 0
    for l in lines:
        l = l.replace('\n', '')
        game = int(l.split(': ')[0].split(' ')[1])
        bags = l.split(': ')[1].split('; ')
        possible = True
        for b in bags:
            cubes = b.split(', ')
            for c in cubes:
                hand = c.split(' ')
                if (hand[1] == 'blue' and int(hand[0]) > max_blues) or (hand[1] == 'green' and int(hand[0]) > max_greens) or (hand[1] == 'red' and int(hand[0]) > max_reds):
                    possible = False
        if possible:
            total += game
    print(total)