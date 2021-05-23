from itertools import accumulate as acc

N, K = map(int, input().split())
P = list(map(int, input().split()))

p = [(1+p_i)/2 for p_i in P]

l = [0] + list(acc(p))

max_num = 0
for i in range(N-K+1):
    s = l[i+K] - l[i]
    max_num = max(s, max_num)

print(max_num)