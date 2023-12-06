file = open('input').read().splitlines()

for line in file:
    if "Time" in line:
        time = list(map(int, line.split(':')[1].split()))
    if "Distance" in line:
        distance = list(map(int, line.split(':')[1].split()))

total = 1
# all races
for i,ms in enumerate(time):
    # one race all times button pressed
    record = 0
    for s in range(ms):
        if s > 0 and ms-s > 0:
            if s*(ms-s) > distance[i]:
                record += 1
    total *= record
print(total)