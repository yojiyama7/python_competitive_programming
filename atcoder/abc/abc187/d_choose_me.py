N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

first_score = 0
scores = []
for a, b in AB:
	scores.append(2*a + b)
	first_score -= a
scores.sort(reverse=True)

def solve(mid):
	# print(mid, first_score, scores[:mid])
	return (first_score + sum(scores[:mid]) >= 1)

ng = 0
ok = N+1
while abs(ok - ng) > 1:
	mid = (ok + ng) // 2
	if solve(mid):
		ok = mid
	else:
		ng = mid

print(ok)
