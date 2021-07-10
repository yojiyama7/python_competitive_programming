N, K = map(int, input().split())

x = N
for _ in range(K):
	if x%200:
		x = int(str(x) + "200")
	else:
		x //= 200

print(x)