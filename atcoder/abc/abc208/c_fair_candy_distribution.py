N, K = map(int, input().split())
A = list(map(int, input().split()))

l = [(a, i) for i, a in enumerate(A)]
l.sort()
l = [(i, idx) for idx, (_, i) in enumerate(l)]
l.sort()

a = K//N
b = K%N
for i, Ai in enumerate(A):
    score = a + (l[i][1] < b)
    print(score)
