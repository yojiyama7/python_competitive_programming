from bisect import bisect, bisect_left, bisect_right

class UnionFind:
    def __init__(self, n):
        self.par = [-1]*n
        self.size = [1]*n
        self.point = n*(n-1) // 2
        self.l = [0]*n

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
        self.l[rx] += self.l[ry]
        return True

    def is_same(self, x, y):
        rx, ry = self.root(x), self.root(y)
        return rx == ry

    def get_size(self, x):
        return self.size[self.root(x)]

    def get_l(self, x):
        return self.l[self.root(x)]

INF = 10**18

L, Q = map(int, input().split())
CX = [list(map(int, input().split())) for _ in range(Q)]

p = [0, L]
for c, x in CX:
    if c == 1:
        p.append(x)
p.sort()
uf = UnionFind(len(p)-1)

for i in range(len(p)-1):
    uf.l[i] = p[i+1] - p[i]

# print(p)

ans_list = []
for c, x in CX[::-1]:
    if c == 1:
        # print([c, x])
        l = bisect_left(p, x)-1
        mid = bisect_left(p, x)
        # print(l, mid)
        uf.unite(l, mid)
    elif c == 2:
        t = bisect_right(p, x)-1
        ans = uf.get_l(t)
        ans_list.append(ans)

print(*ans_list[::-1], sep='\n')
