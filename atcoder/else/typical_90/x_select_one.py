N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cost = sum(abs(a-b) for a, b in zip(A, B))

if cost <= K and (K-cost)%2 == 0:
	print("Yes")
else:
	print("No")
