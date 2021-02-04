from collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter([tuple(sorted([i, a-1])) for i, a in enumerate(A)])

# print(c)
print(sum([v==2 for _, v in c.items()]))