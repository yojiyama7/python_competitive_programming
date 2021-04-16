# 問題文の X, Y のつかいかたきも

H, W, Y, X = map(int, input().split())
S = [input() for _ in range(H)]

X, Y = X-1, Y-1

cnt = -3
for x in range(X, -1, -1):
	if S[Y][x] == '#':
		break
	cnt += 1
for x in range(X, W):
	if S[Y][x] == '#':
		break
	cnt += 1
for y in range(Y, -1, -1):
	if S[y][X] == '#':
		break
	cnt += 1
for y in range(Y, H):
	if S[y][X] == '#':
		break
	cnt += 1

print(cnt)