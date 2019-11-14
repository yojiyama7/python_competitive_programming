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

################################
