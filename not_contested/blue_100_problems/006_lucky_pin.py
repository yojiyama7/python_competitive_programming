# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d

N = int(input())
S = input()

l = list(map(int, S[::-1]))

cnt = 0
for i in range(1000):
	j = 0
	for k in range(N):
		if i//(10**j)%10 == l[k]:
			j += 1
		if j == 3:
			cnt += 1
			break

print(cnt)
