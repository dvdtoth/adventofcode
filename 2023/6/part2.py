file = open('input').read().splitlines()

for line in file:
    if "Time" in line:
        time = int(line.split(':')[1].replace(" ", ""))
    if "Distance" in line:
        distance = int(line.split(':')[1].replace(" ", ""))

record = 0
for s in range(time):
    if s > 0 and time-s > 0:
        if s*(time-s) > distance:
            record += 1
print(record)