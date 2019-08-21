import heapq

N, M = map(int, input().split(" "))
AB = [list(map(int, input().split(" "))) for _ in range(N)]
# N, M = (10**5, 10**5)
# AB = [(i, i//100) for i in range(N)]

l = [[] for _ in range(10**5+1)]
for a, b in AB:
    l[a].append(b)
l = [sorted(l_i, reverse=True) for l_i in l]

l = [[(-l_j, l_j) for l_j in l_i] for l_i in l]

point = 0
p = []
for i in range(M, -1, -1):
    for l_j in l[M-i]:
        heapq.heappush(p, l_j)
    # print(p)
    if p == []:
        continue
    point += heapq.heappop(p)[1]

print(point)