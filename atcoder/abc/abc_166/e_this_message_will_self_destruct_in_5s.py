# (i < j)
# j - i = A[i] + A[j]
# j - A[j] = i + A[i]
# (i >= j)
# i - j = A[i] + A[j]
# i - A[i] = j + A[j]

from collections import Counter

N = int(input())
A = list(map(int, input().split()))

p = [i+Ai for i, Ai in zip(range(1, N+1), A)]
q = [j-Aj for j, Aj in zip(range(1, N+1), A)]

pc = Counter(p)
qc = Counter(q)

r = sum(pc[k]*qc[k] for k in pc.keys() & qc.keys())

print(r)