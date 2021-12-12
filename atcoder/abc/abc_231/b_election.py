from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

l = list(Counter(S).items())
l.sort(key=lambda kv: kv[1])
ans = l[-1][0]
print(ans)
