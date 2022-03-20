# AC

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]


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


uf = UnionFind(N)
results = []
for a, b in AB[::-1]:
    results.append(uf.point)
    x, y = a-1, b-1
    uf.unite(x, y)

print(*results[::-1], sep="\n")

################################

# # 原因不明のTLE

# import sys
# sys.setrecursionlimit(10**8)

# input = sys.stdin.readline

# N, M = map(int, input().split())
# AB = [list(map(int, input().split())) for _ in range(M)]


# class UnionFind:
#     def __init__(self, n):
#         self.n = n
#         self.per = list(range(n))
#         self.point = n*(n-1) // 2
#         self.counts = [1]*n
#         self.rank = [0]*n

#     def root(self, x):
#         # while self.per[x] != x:
#         #     x = self.per[x]
#         # return x
#         if self.per[x] == x:
#             return x
#         else:
#             self.per[x] = self.root(self.per[x])
#             return self.per[x]

#     def unite(self, x, y):
#         rx = self.root(x)
#         ry = self.root(y)
#         if rx == ry:
#             return False
#         if self.rank[rx] < self.rank[ry]:
#             self.per[rx] = ry
#         else:
#             self.per[ry] = rx
#             if self.rank[rx] == self.rank[ry]:
#                 self.rank[rx] += 1
#         self.point -= self.counts[ry] * self.counts[rx]
#         self.counts[ry] += self.counts[rx]
#         self.counts[rx] = 0

#     def is_same(self, x, y):
#         rx = self.root(x)
#         ry = self.root(y)
#         return rx == ry


# u = UnionFind(N)
# results = []
# for a, b in AB[::-1]:
#     results.append(u.point)
#     x, y = a-1, b-1
#     u.unite(x, y)

# # print(*results[::-1])
# for r in results[::-1]:
#     print(r)
