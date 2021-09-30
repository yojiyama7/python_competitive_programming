from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))

l = Counter(A)
p = sorted(l.items(), key=lambda x: -x[1])
# print(p)
if p[0][1] > N/2:
    print(p[0][0])
else:
    print('?')