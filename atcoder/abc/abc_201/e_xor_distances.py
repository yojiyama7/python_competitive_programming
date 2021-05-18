# 解説読んだ
# 考察して、きちんと整理しきってから書くだけ
# 整理しきる前に書くとごちゃる
# 帰着した問題を文字化して書いておく
# 各種値の変数名を決めておく(その名前で証明を書く)

# pypy AC

from collections import deque

MOD = 10**9+7

N = int(input())
UVW = [list(map(int, input().split())) for _ in range(N-1)]

g = [set() for _ in range(N)]
for u, v, w in UVW:
	u, v = u-1, v-1
	g[u].add((v, w))
	g[v].add((u, w))

d = [-1]*N
d[0] = 0
q = deque([0])
while q:
	t = q.popleft()
	t_d = d[t]

	for to, cost in g[t]:
		if d[to] != -1:
			continue
		d[to] = t_d ^ cost
		q.append(to)

ans = 0
for i in range(60):
	l = [0, 0]
	for d_j in d:
		l[(d_j>>i)&1] += 1
	ans += (l[0]*l[1])%MOD * pow(2, i, MOD)
	ans %= MOD

print(ans)
