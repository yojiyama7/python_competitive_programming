K = int(input())
S = input()
T = input()

def solve_score(l):
	score = 0
	for i in range(1, 10):
		score += i*10**l.count(i)
	return (score)

l = [K]*10
for s in S[:4]:
	l[int(s)] -= 1
for t in T[:4]:
	l[int(t)] -= 1

remain = 9*K-8

cnt = 0
for i in range(1, 10):
	for j in range(1, 10):
		takahashi = solve_score(list(map(int, S[:4])) + [i])
		aoki = solve_score(list(map(int, T[:4])) + [j])
		if takahashi > aoki:
			p = (l[i]/remain) * ((l[j] - (i == j))/(remain - 1))
			cnt += p

print(cnt)
