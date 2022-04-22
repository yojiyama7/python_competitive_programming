from collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter(A)
for k, v in c.items():
    if v == 3:
        print(k)
        break