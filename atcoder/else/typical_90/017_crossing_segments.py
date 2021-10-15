# あまりにもわからない
# というよりたんにデータ構造の難易度が高かったり
# 制度(訂正: 精度)を持って思考が運べなくなってきたので回答を見ます

# 答え見たら全然違うアプローチ
# 条件を式にして云々と書いてある
# 辺を追加していって、それによって交差ような (s, t) を数えるのはありな気がするが
# データ構造を

################################

# # 方針詰めが甘い
# # けどなぜかわかるのは具体的に書いたからなのでえらい

# # from icecream import ic
# # print = ic

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

# # 1-indexed 閉区間 add_range sum_point
# class Bit2:
# 	def __init__(self, n):
# 		self.n = n
# 		self.bit = Bit(n+1)

# 	def add(self, a, b, w=1):
# 		self.bit.add(a, w)
# 		self.bit.add(b+1, -w)
# 		# print(self.bit.sum(self.n+1))

# 	def sum(self, a):
# 		return (self.bit.sum(a))

# N, M = map(int, input().split())
# LR = [list(map(int, input().split())) for _ in range(M)]

# # 各頂点から行けない場所をカウントする
# bit = Bit2(N)
# for l, r in LR:
# 	bit.add(l, l, 1)
# 	bit.add(r, r, 1)

# 	size1 = r-l
# 	size2 = N-size1
# 	print(l, r, size1, size2)
# 	bit.add(l+1, r-1, size2-1)
# 	bit.add(1, l-1, size1-1)
# 	bit.add(r+1, N, size1-1)
# 	print([bit.sum(i) for i in range(1, N+1)])

# sum_num = 0
# for i in range(1, N+1):
# 	# print(i, bit.sum(i))
# 	sum_num += N-1 - bit.sum(i)

# print(sum_num)