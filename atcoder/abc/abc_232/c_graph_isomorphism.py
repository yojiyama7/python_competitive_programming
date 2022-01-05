from itertools import permutations as permu

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
CD = [list(map(int, input().split())) for _ in range(M)]

AB = {tuple(sorted([a, b])) for a, b in AB}

for l in permu(range(1, N+1)):
    edges = set()
    for c, d in CD:
        c -= 1
        d -= 1
        edge = tuple(sorted([l[c], l[d]]))
        edges.add(edge)
    # print(AB, edges, l)
    if AB == edges:
        print("Yes")
        exit()
print("No")
