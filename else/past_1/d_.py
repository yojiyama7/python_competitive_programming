from collections import Counter

N = int(input())
A = [int(input()) for _ in range(N)]

a = Counter(A)
x = Counter(range(1, N+1))

if len(x - a) == 0:
    print("Correct")
else:
    b = sorted(a, key=lambda k: a[k])[-1]
    print(b, list(x - a)[0])