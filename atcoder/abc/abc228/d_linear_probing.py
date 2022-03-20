class UnionFind:
    def __init__(self, n):
        self.par = [-1]*n
        self.size = [1]*n
        # 右方向に一番近い、次に要素を入れることが可能な場所
        self.right = list(range(n))

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
        self.right[rx] = self.right[ry]
        # size において rx>ry にする
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.size[rx] += self.size[ry]
        # ryの親をrxに設定 (sizeにおいて "小さい方(ry)を大きい方(rx)に" つなげる)
        self.par[ry] = rx
        # y の右端が合体後の右端となる
        return True

    def is_same(self, x, y):
        rx, ry = self.root(x), self.root(y)
        return rx == ry

    def get_size(self, x):
        return self.size[self.root(x)]

Q = int(input())
TX = [list(map(int, input().split())) for _ in range(Q)]

N = 1<<20
# N = 10
A = [-1 for _ in range(N)]
uf = UnionFind(N)

for t, x in TX:
    if t == 1:
        empty = uf.right[uf.root(x%N)]
        uf.unite(empty, (empty+1)%N)
        A[empty] = x
    if t == 2:
        print(A[x%N])
# print(A)
# print(uf.par)
# print([uf.right[uf.root(x)] for x in range(N)])

################################

# # この実装だと既に追加してある範囲の左側に要素を書き込むとバグる
# # 連続する部分を塊としてとらえるような実装が良い(両端をまたいで連続する可能性に注意する)

# # 1-indexed 閉区間 add_point sum_range
# class Bit:
#     def __init__(self, n):
#         self.n = n
#         self.array = [0]*(n+1)

#     def add(self, x, w=1):
#         # print(f"{id(self)}: Bit.add({x}, {w})")
#         while (x <= self.n):
#             self.array[x] += w
#             x += (x & -x)
#     def add0idx(self, x, w=1):
#         self.add(x+1, w)

#     def sum(self, x, y=None):
#         # print(f"{id(self)}: Bit.sum({x}, {y})")
#         if y == None:
#             # 1~x
#             sum_num = 0
#             while (x > 0):
#                 sum_num += self.array[x]
#                 x -= (x & -x)
#             return sum_num
#         else:
#             # x~y
#             return self.sum(y) - self.sum(x-1)
#     def sum0idx(self, x, y=None):
#         return self.sum(x+1, None if y == None else y+1)

# Q = int(input())
# TX = [list(map(int, input().split())) for _ in range(Q)]

# N = 1<<20
# a = [-1]*N
# # 0 ~ N
# next_empty = Bit(N+1)

# for t, x in TX:
#     if t == 1:
#         h = x%N
#         empty = h + next_empty.sum0idx(h)
#         a[empty] = x
#         if x%N == N-1:
#             continue
#         if empty < N:
#             next_empty.add0idx(h, 1)
#             next_empty.add0idx(empty+1, -1)
#         else:
#             empty %= N
#             next_empty.add0idx(h, 1)
#             next_empty.add0idx(0, 1)
#             next_empty.add0idx(empty+1, -1)
#     else:
#         ans = a[x%N]
#         print(ans)
#     # print([next_empty.sum0idx(i) for i in range(N)], a)
