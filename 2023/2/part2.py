
# read file line by line
with open('input') as f:
    lines = f.readlines()

    total = 0
    for l in lines:
        l = l.replace('\n', '')
        game = int(l.split(': ')[0].split(' ')[1])
        bags = l.split(': ')[1].split('; ')
        min_blue = -1
        min_red = -1
        min_green = -1
        for b in bags:
            cubes = b.split(', ')
            for c in cubes:
                hand = c.split(' ')
                if (hand[1] == 'blue' and int(hand[0]) > min_blue):
                    min_blue = int(hand[0])
                if (hand[1] == 'red' and int(hand[0]) > min_red):
                    min_red = int(hand[0])
                if (hand[1] == 'green' and int(hand[0]) > min_green):
                    min_green = int(hand[0])
        total += min_blue * min_red * min_green
    print(total)
