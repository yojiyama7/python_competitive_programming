from collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter(a%200 for a in A)
ans = 0
for x in c.values():
	ans += x*(x-1)//2

print(ans)
