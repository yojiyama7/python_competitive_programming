N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort()
pos = K
for a, b in AB:
	if pos < a:
		break
	pos += b

print(pos)
