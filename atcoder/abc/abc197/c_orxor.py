INF = float('inf')

N = int(input())
A = list(map(int, input().split()))

def or_list(l):
	x = 0
	for l_i in l:
		x |= l_i
	return (x)

min_num = INF
for i in range(1<<(N-1)):
	res = 0
	b = 0
	for j in range(N-1):
		if i&(1<<j):
			res ^= or_list(A[b:j+1])
			b = j+1
	res ^= or_list(A[b:N])
	min_num = min(res, min_num)

print(min_num)
