from collections import deque, Counter

MOD = 998244353
INF = 10**18

N = int(input())
UV = [list(map(int, input().split())) for _ in range(N-1)]

g = [set() for _ in range(N)]
for u, v in UV:
    u -= 1
    v -=  1
    g[u].add(v)
    g[v].add(u)

dist = [INF]*N
dist[0] = 0
q = deque([0])
is_leaf = [0]*N
while q:
    t = q.popleft()
    flag = 0
    for to in g[t]:
        if dist[to] <= dist[t]+1:
            continue
        flag = 1
        dist[to] = dist[t]+1
        q.append(to)
    if not flag:
        is_leaf[t] = 1
l = [dist[i] for i in range(N) if is_leaf[i]]

if len(set(l[1:])) == 1:
    x = len(l)
    ans = x * (x-1) * pow(2, MOD-2, MOD)
print(l)

x, y = sorted(set(l))[-2:]

l_counter = Counter(l)

a = l_counter[x]
b = l_counter[y]
print(a, b, (2**a, 2**b))

ans = (a * b) % MOD
print(ans)