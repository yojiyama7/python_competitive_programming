from collections import deque

INF = float('inf')

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]
Q = int(input())
TEX = [list(map(int, input().split())) for _ in range(Q)]

AB_0idx = [(a-1, b-1) for a, b in AB]
A_0idx, B_0idx = zip(*AB_0idx)

g = [set() for _ in range(N)]
for a, b in AB_0idx:
	g[a].add(b)
	g[b].add(a)

depth = [INF]*N
depth[0] = 0
q = deque([0])
while q:
	t = q.popleft()
	for child in g[t]:
		if depth[child] <= depth[t] + 1:
			continue
		depth[child] = depth[t] + 1
		q.append(child)

score = [0]*N
for t, e, x in TEX:
	t, e, x = t, e-1, x
	ref, obs = A_0idx[e], B_0idx[e]
	if t == 2:
		ref, obs = obs, ref
	# depth[ref] != depth[obs]
	if depth[ref] < depth[obs]:
		score[0] += x
		score[obs] -= x
	else:
		score[ref] += x
	# print(score)

q = deque([0])
while q:
	t = q.popleft()
	# print(t, q, g[t])
	for child in g[t]:
		if depth[child] <= depth[t]:
			continue
		# print(child)
		score[child] += score[t]
		# print(f"{child} <- {t}")
		q.append(child)

print(*score, sep='\n')
