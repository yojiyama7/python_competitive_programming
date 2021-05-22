N = int(input())
A, B, C = [list(map(int, input().split())) for _ in range(3)]

l = [0]*(N+1)
for c in C:
	idx = B[c-1]
	l[idx] += 1

ans = 0
for a in A:
	ans += l[a]

print(ans)
