from itertools import accumulate as acc
from bisect import bisect

INF = float("inf")

N, M = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))

H.sort()
W.sort()

q = [-INF] + W + [INF]
# print(q)

p = []
for i in range(N-1):
    p.append(H[i+1] - H[i])

p_left_acc = [0] + list(acc([p_i if i%2 == 0 else 0 for i, p_i in enumerate(p)]))
p_right_acc = [0] + list(acc([p_i if i%2 == 1 else 0 for i, p_i in enumerate(p)]))

min_num = INF
for i in range(0, N, 2):
    # print(i, N-1)
    cost = 0
    cost += p_right_acc[N-1] - p_right_acc[i]
    cost += p_left_acc[i] - p_left_acc[0]
    idx = bisect(q, H[i])
    # print(idx)
    cost += min(abs(q[idx]-H[i]), abs(q[idx-1]-H[i]))
    min_num = min(min_num, cost)

print(min_num)
