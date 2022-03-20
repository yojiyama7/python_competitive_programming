from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

S = ["".join(sorted(s)) for s in S]

print(sum([m*(m-1) for m in Counter(S).values()])//2)