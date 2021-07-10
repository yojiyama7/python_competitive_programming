from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

counter = Counter(S)

for k in ["AC", "WA", "TLE", "RE"]:
    print(k, "x", counter[k])