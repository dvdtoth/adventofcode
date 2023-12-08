file = open('input').read().splitlines()

order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

bids = {}
hands = []
hands_lists = []

for l in file:
    bids[l.split(' ')[0]] = l.split(' ')[1]
    hands += [l.split(' ')[0]]
    hands_lists += map(list, l.split(' ')[0].split())

def same_kind(input_list):
    labels = set(item for item in input_list if input_list.count(item) > 1)
    strength = 0

    for item in labels:
        a = False
        kind = input_list.count(item)
        # five = 6, four = 5
        if kind > 3:
            strength = kind + 1
        if kind < 3 and strength == 0:
            # two = 1, one = 0
            strength = kind -1
            a = True
        if (kind == 2 and strength == 3) or (kind == 3 and strength == 1):
            # full house = 4
            strength = 4
            continue
        if strength == 1 and kind == 2 and a == False:
            # two pairs = 2
            strength = 2
        if kind == 3:
            # three = 3
            strength = kind

    # handle jokers
    if 'J' in input_list:
        new_list = input_list.copy()
        jc = new_list.count('J')
        if jc == 5:
            strength = 6
        if jc < 5:
            # remove all instances of J
            new_list = [x for x in new_list if x != 'J']
            # replace with whichever has the highest count
            max = 0
            for l in new_list:
                if new_list.count(l) > max:
                    max = new_list.count(l)
                    ch = l
            for _ in range(jc):
                new_list.append(ch)
            strength = same_kind(new_list)

    return strength


by_s = {k: [] for k in range(7)}

# sort all hands by strength
for i,h in enumerate(hands_lists):
    strength = same_kind(h)
    by_s[strength] += [hands[i]]

# loop all strenghts and sort by custom order
final = []
for i in reversed(range(7)):
    final += sorted(by_s[i], key=lambda word: [order.index(c) for c in word])


# multiply by bids
total = 0
for j,h in enumerate(reversed(final)):
    total += int(bids[h]) * int(j+1)

print(total)
