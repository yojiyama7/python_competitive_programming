# 操作を二種類に分ける 
# 素因数分解が√Nで行ける
# UnionFind の unite が小さいほうを大きいほうに連結する
# 等に似ている
# コストの低いものは愚直に、高いものは更新時にそのコストを後回しにして解く
# 1. コストの低いものによる愚直なコスト
# 2. コストの高い物によって後回しにされるコスト
# これらのバランスに √cost が絡んでくることが多い

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

N, M, Q = map(int, input().split())
UV = [list(map(int, input().split())) for _ in range(M)]
X = list(map(int, input().split()))

g1 = [set() for i in range(N)]
for u, v in UV:
    u -= 1
    v -= 1
    g1[u].add(v)
    g1[v].add(u)

p = [-1]*N
for x in X[::-1]:
    x -= 1
    print(x, p)
    for to in g1[x]:
        p[to] = x
    g1[x] = set()

uf = UnionFind(N)
for i, pi in enumerate(p):
    uf.unite(i, pi)

print(*[uf.root(i) for i in range(N)])
