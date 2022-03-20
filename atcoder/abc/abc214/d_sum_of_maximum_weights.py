class UnionFind:
    def __init__(self, n):
        self.par = [-1]*n
        self.size = [1]*n
        self.point = n*(n-1) // 2

    def root(self, x):
        if self.par[x] < 0:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False
        # size において rx>ry にする
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.point -= self.size[rx]*self.size[ry]
        self.size[rx] += self.size[ry]
        # ryの親をrxに設定 (sizeにおいて "小さい方(ry)を大きい方(rx)に" つなげる)
        self.par[ry] = rx
        return True

    def is_same(self, x, y):
        rx, ry = self.root(x), self.root(y)
        return rx == ry

    def get_size(self, x):
        return self.size[self.root(x)]

N = int(input())
UVW = [list(map(int, input().split())) for _ in range(N-1)]

uf = UnionFind(N)

UVW.sort(key=lambda x: x[2])

ans = 0
for u, v, w in UVW:
    u -= 1
    v -= 1
    ans += w * uf.get_size(u) * uf.get_size(v)
    # print((u, v), w, uf.get_size(u), uf.get_size(v))
    uf.unite(u, v)

print(ans)

################################

# INF = 10**18

# N = int(input())
# UVW = [list(map(int, input().split())) for _ in range(N-1)]

# g = [set() for _ in range(N)]
# for u, v, w in UVW:
#     u -= 1
#     v -= 1
#     g[u].add(v)
#     g[v].add(u)

# cnt = [1]*N
# depth = [INF]*N
# def dfs(i, d):
#     depth[i] = d
#     for to in g[i]:
#         if depth[to] < d:
#             continue
#         dfs(to, d+1)
#         cnt[i] += cnt[to]
# dfs(0, 0)
# print(cnt, depth)

# ans = 0
# for u, v, w in sorted(UVW, lambda x:x[2], reverse=True):
#     u -= 1
#     v -= 1
#     if depth[u] > depth[v]:
#         u, v = v, u
#     ans += w * cnt[v]*(N-cnt[v])

################################

# INF = 10**18

# N = int(input())
# UVW = [list(map(int, input().split())) for _ in range(N-1)]

# g = [set() for _ in range(N)]
# for u, v, w in UVW:
#     u -= 1
#     v -= 1
#     g[u].add(v)
#     g[v].add(u)

# visited = []
# pre = [None]*N
# depth = [INF]*N
# def dfs(v, d):
#     pre[v] = len(visited)
#     depth[v] = d
#     visited.append(v)
#     for w in g[v]:
#         for depth[w] < d:
#             continue
#         dfs(w, d+1)
#         visited.append(v)
# dfs(0, 0)

# print(visited, pre)