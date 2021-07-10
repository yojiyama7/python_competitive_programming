# 大 に対して 小 を結合することで 計算量を抑える

class UnionFind:
    def __init__(self, n, l):
        self.par = [-1]*n
        self.size = [1]*n
        self.point = n*(n-1) // 2
        self.l = [{l_i: 1} for l_i in l]
        self.l_size = [1]*n

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
        a, b = self.l[rx], self.l[ry]
        if self.l_size[rx] < self.l_size[ry]:
            a, b = b, a
        self.l[rx] = a
        for k, v in b.items():
            if k not in self.l[rx]:
                self.l[rx][k] = 0
            self.l[rx][k] += v
        return True

    def is_same(self, x, y):
        rx, ry = self.root(x), self.root(y)
        return rx == ry

    def get_size(self, x):
        return self.size[self.root(x)]
    
    def get_l(self, x, y):
        a = self.l[self.root(x)]
        if y not in a:
            return 0
        return a[y]

N, Q = map(int, input().split())
C = list(map(int, input().split()))
QUERY = [list(map(int, input().split())) for _ in range(Q)]
# N, Q = 20000, 20000
# C = [i%10 for i in range(N)]
# QUERY = [(2, (i*2)%N, (i*2+1)%N) for i in range(Q)]

uf = UnionFind(N, C)

for kind, a, b in QUERY:
    if kind == 1:
        a, b = a-1, b-1
        uf.unite(a, b)
    if kind == 2:
        x, y = a-1, b
        print(uf.get_l(x, y))
