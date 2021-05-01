# なんでこれで解けるの
# 計算量わかんね

INF = float('inf')

N = int(input())
A = list(map(int, input().split()))

memo = [[INF for _ in range(2*N+1)]for _ in range(2*N)]
def solve(l, r):
	# print(l, r)
	if r-l == 0:
		return (0)
	elif r-l == 2:
		return abs(A[l]-A[l+1])
	if memo[l][r] == INF:
		for i in range(l+2, r, 2):
			score = solve(l, i) + solve(i, r)
			memo[l][r] = min(score, memo[l][r])
		memo[l][r] = min(
			solve(l+1, r-1) + abs(A[l]-A[r-1]),
			memo[l][r]
		)
	return memo[l][r]

print(solve(0, 2*N))

################################

# INF = float('inf')

# N = int(input())
# A = list(map(int, input().split()))

# # O(2**N)? で解く

# min_num = INF
# for i in range(1<<2*N):
# 	stack = []
# 	cost = 0
# 	is_valid = True
# 	for j in range(2*N):
# 		if (i>>j)&1:
# 			stack.append(A[j])
# 		else:
# 			if not stack:
# 				is_valid = False
# 				break
# 			cost += abs(A[j]-stack.pop())
# 	# print(bin(i)[2:], cost)
# 	if is_valid and len(stack) == 0:
# 		min_num = min(
# 			cost,
# 			min_num
# 		)

# print(min_num)
