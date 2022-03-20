H, W = map(int, input().split())
Q = int(input())
QUERY = [list(map(int, input().split())) for _ in range(Q)]

class UnionFind:
    def __init__(self, n):
        self.par = [-1]*n
        self.size = [1]*n
        # self.point = n*(n-1) // 2

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
        # self.point -= self.size[rx]*self.size[ry]
        self.size[rx] += self.size[ry]
        # ryの親をrxに設定 (sizeにおいて "小さい方(ry)を大きい方(rx)に" つなげる)
        self.par[ry] = rx
        return True

    def is_same(self, x, y):
        rx, ry = self.root(x), self.root(y)
        return rx == ry

    def get_size(self, x):
        return self.size[self.root(x)]

is_red = [[0 for _ in range(W)] for _ in range(H)]

uf = UnionFind(H*W)
def to_idx(r, c):
	return W*r + c

for t, *l in QUERY:
	if t == 1:
		r, c = l
		r, c = r-1, c-1
		is_red[r][c] = 1
		for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
			cr, cc = r+dr, c+dc
			if not (0 <= cr < H and 0 <= cc < W):
				continue
			if is_red[cr][cc]:
				uf.unite(to_idx(r, c), to_idx(cr, cc))
	else:
		ra, ca, rb, cb = l
		ra, ca, rb, cb = ra-1, ca-1, rb-1, cb-1
		idx1 = to_idx(ra, ca)
		idx2 = to_idx(rb, cb)
		if is_red[ra][ca] and is_red[rb][cb] and uf.is_same(idx1, idx2):
			print("Yes")
		else:
			print("No")

################################

# # WA

# # 1重配列での実装ではあるものの、上で通るのになぜこれ通らん？

# class UnionFind:
#     def __init__(self, n):
#         self.par = [-1]*n
#         self.size = [1]*n
#         # self.point = n*(n-1) // 2

#     def root(self, x):
#         if self.par[x] < 0:
#             return x
#         self.par[x] = self.root(self.par[x])
#         return self.par[x]

#     def unite(self, x, y):
#         rx = self.root(x)
#         ry = self.root(y)
#         if rx == ry:
#             return False
#         # size において rx>ry にする
#         if self.size[rx] < self.size[ry]:
#             rx, ry = ry, rx
#         # self.point -= self.size[rx]*self.size[ry]
#         self.size[rx] += self.size[ry]
#         # ryの親をrxに設定 (sizeにおいて "小さい方(ry)を大きい方(rx)に" つなげる)
#         self.par[ry] = rx
#         return True

#     def is_same(self, x, y):
#         rx, ry = self.root(x), self.root(y)
#         return rx == ry

#     def get_size(self, x):
#         return self.size[self.root(x)]

# H, W = map(int, input().split())
# Q = int(input())
# Query = [list(map(int, input().split())) for _ in range(Q)]
# # H, W = 11, 11
# # Query = [
# # 	[1, i//W+1, i%W+1] for i in range(0, H*W, 2)
# # ] + [
# # 	# [2, i//W+1, i%W+1, j//W+1, j%W+1] for i, j in product(range(H*W), repeat=2)
# # 	[2, i//W+1, i%W+1, i//W+1, i%W+1] for i in range(H*W)
# # ]
# # Q = len(Query)

# uf = UnionFind(H*W)

# is_red = [0]*(H*W)

# for q in Query:
# 	t = q[0]
# 	if t == 1:
# 		_, r, c = q
# 		# k = False
# 		# if r == 3 and c == 2:
# 		# 	k = True
# 		r, c = r-1, c-1
# 		idx = W*r + c
# 		is_red[idx] = 1
# 		if idx-1 >= 0 and is_red[idx-1]:
# 			# if k:
# 			# 	print('a')
# 			uf.unite(idx, idx-1)
# 		if idx+1 < H*W and is_red[idx+1]:
# 			# if k:
# 			# 	print('b')
# 			uf.unite(idx, idx+1)
# 		if idx-W >= 0 and is_red[idx-W]:
# 			# if k:
# 			# 	print('c')
# 			uf.unite(idx, idx-W)
# 		if idx+W < H*W and is_red[idx+W]:
# 			# if k:
# 			# 	print('d')
# 			uf.unite(idx, idx+W)
# 		# if k:
# 		# 	print("--")
# 	elif t == 2:
# 		_, r1, c1, r2, c2 = q
# 		r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
# 		idx1 = W*r1 + c1
# 		idx2 = W*r2 + c2
# 		if is_red[idx1] and is_red[idx2] and uf.is_same(idx1, idx2):
# 			print("Yes")
# 		else:
# 			print("No")
# 	# print(f"<<{q}>>")
# 	# for i in range(H):
# 	# 	print(is_red[W*i:W*(i+1)])

# 	# for i in range(H):
# 	# 	print(*[uf.root(j) for j in range(W*i, W*(i+1))])


# # for i in range(H):
# # 	print(is_red[W*i:W*(i+1)])

# # for i in range(H):
# # 	print(*[uf.root(j) for j in range(W*i, W*(i+1))])
# 	# print(uf.par[W*i:W*(i+1)])
