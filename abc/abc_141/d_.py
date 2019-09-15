from heapq import *

N, M = map(int, input().split())
A = list(map(int, input().split()))

# print(A)
A = [-a for a in A]
heapify(A)
# print(A)
for _ in range(M):
    x = -heappop(A)
    heappush(A, -(x/2))

print(sum([int(-a) for a in A]))