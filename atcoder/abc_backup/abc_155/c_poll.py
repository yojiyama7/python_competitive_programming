from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

c = Counter(S)
c_max = max(c.values())
[print(x) for x in sorted([s for s in set(S) if c[s] == c_max])]