# 実装 重い

from bisect import bisect_left, bisect_right

INF = float('inf')

N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

# k番目が neg, zero, pos のどれであるか判定
neg = 0
neg_absnums = []
zero = 0
pos = 0
pos_nums = []
for a in A:
	if a == 0:
		zero += 1
	elif a < 0:
		neg += 1
		neg_absnums.append(abs(a))
	else:
		pos += 1
		pos_nums.append(a)
neg_absnums.reverse()

all = N*(N-1)//2
all_pos = pos*(pos-1)//2 + neg*(neg-1)//2
all_neg = pos*neg
all_zero = zero*(N-1) - zero*(zero-1)//2

# if not (all_pos + all_zero + all_neg == all):
# 	print(all_pos, all_zero, all_neg, all, "??")

def is_ok_inner_neg(x):
	ans = 0
	for a in neg_absnums:
		b_min = -(x//a)
		b_cnt = len(pos_nums) - bisect_left(pos_nums, b_min)
		ans += b_cnt
	return ans

def is_ok_inner_pos(x):
	ans_1 = 0
	for a in pos_nums:
		b_max = x//a
		b_cnt = bisect_right(pos_nums, b_max) - (a <= b_max)
		ans_1 += b_cnt
	# print(ans_1)
	ans_1 //= 2
	ans_2 = 0
	for a in neg_absnums:
		b_max = x//a
		b_cnt = bisect_right(neg_absnums, b_max) - (a <= b_max)
		ans_2 += b_cnt
	# print(ans_2)
	ans_2 //= 2
	ans = all_neg + all_zero + ans_1 + ans_2
	return ans

# K <= 積がx以下になるものの個数 であるか
def is_ok(x):
	ans = 0
	if x < 0:
		ans = is_ok_inner_neg(x)
	elif x == 0:
		ans = all_neg + all_zero
	else:
		ans = is_ok_inner_pos(x)
	# print(x, ans, K <= ans)
	return (K <= ans)

ok, ng = 10**18+1, -(10**18+1)
while abs(ok - ng) > 1:
	mid = (ok + ng) // 2
	if is_ok(mid):
		ok = mid
	else:
		ng = mid

print(ok)

################################

# 正負の数の積に関するものは、積が負, 0, 正になるパターンで場合分けする
# K番目(二分探索感)

# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# A.sort()

################################

# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# A.sort()

# K

# # l = []
# # m = []
# # for i, a in enumerate(A):
# #     for j, b in enumerate(A):
# #         if i < j:
# #             l.append(a*b)
# #             m.append((a, b))

# # l.sort()

# # print(l[K-1])

# # [print(x) for x in sorted(m, key=lambda x: x[0]*x[1])]