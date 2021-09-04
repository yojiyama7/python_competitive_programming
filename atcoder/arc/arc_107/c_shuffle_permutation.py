MOD = 998244353

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

N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

row_uf = UnionFind(N)
column_uf = UnionFind(N)

for i in range(N):
    for j in range(N):
        if all(a+b<=K for a, b in zip(A[i], A[j])):
            row_uf.unite(i, j)

for i in range(N):
    for j in range(N):
        if all(a[i]+a[j]<=K for a in A):
            column_uf.unite(i, j)

fact_memo = [None]*(N+1)
def fact(x):
    if x == 0:
        return 1
    if fact_memo[x] == None:
        fact_memo[x] = x * fact(x-1)
        fact_memo[x] %= MOD
    return fact_memo[x]

ans = 1
for i in range(N):
    if row_uf.root(i) == i:
        ans *= fact(row_uf.get_size(i))
        ans %= MOD
    if column_uf.root(i) == i:
        ans *= fact(column_uf.get_size(i))
        ans %= MOD

print(ans)
