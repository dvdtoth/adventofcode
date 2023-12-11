from collections import deque

file = open('input').read().splitlines()

directions = {
"|": [(1, 0), (-1, 0)],
"-": [(0, 1), (0, -1)],
"L": [(-1, 0), (0, 1)],
"J": [(-1, 0), (0, -1)],
"7": [(1, 0), (0, -1)],
"F": [(1, 0), (0, 1)],
".": [],
}

def neighbours(i, j):
    res = []
    for di, dj in list(direct_neighbours(i, j)):
        ii, jj = i + di, j + dj
        if not (0 <= ii < len(file) and 0 <= jj < len(file[0])):
            continue
        res.append((ii, jj))
    return res


def direct_neighbours(i, j):
    res = []
    if file[i][j] == "S":
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ii, jj = i + di, j + dj
            if not (0 <= ii < len(file) and 0 <= jj < len(file[0])):
                continue
            if (i, j) in list(neighbours(ii, jj)):
                res.append((di, dj))
        return res

    else:
        # map neighbours
        return directions[file[i][j]]


si, sj = None, None
for i, line in enumerate(file):
    if "S" in line:
        si, sj = i, line.index("S")
        break


# Breadth-First Search (BFS)
visited = set()
dists = {}
q = deque([((si, sj), 0)])
while len(q) > 0:
    top, dist = q.popleft()
    if top in visited:
        continue
    visited.add(top)
    dists[top] = dist

    for nbr in list(neighbours(*top)):
        if nbr in visited:
            continue
        q.append((nbr, dist + 1))

ans = max(dists.values())
print(ans)