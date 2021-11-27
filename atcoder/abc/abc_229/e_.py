class UnionFind:
    def __init__(self, n):
        self.par = [-1]*n
        self.size = [1]*n
        self.count = n

    def root(self, x):
        if self.par[x] == -1:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False
        self.count -= 1
        # size において rx>ry にする
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.size[rx] += self.size[ry]
        # ryの親をrxに設定 (sizeにおいて "小さい方(ry)を大きい方(rx)に" つなげる)
        self.par[ry] = rx
        return True

    def is_same(self, x, y):
        rx, ry = self.root(x), self.root(y)
        return rx == ry

    def get_size(self, x):
        return self.size[self.root(x)]

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

edges = [set() for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    if a < b:
        edges[a].add(b)
    else:
        edges[b].add(a)

ans = [None]*N
uf = UnionFind(N)
for i in reversed(range(N)):
    ans[i] = uf.count-i-1
    for to in edges[i]:
        uf.unite(i, to)

print(*ans, sep='\n')
