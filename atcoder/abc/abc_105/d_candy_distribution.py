# 累積和 MOD

from itertools import accumulate as acc
from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))

l = [0] + list(acc(A)) # A_acc
l = [l_i%M for l_i in l]

ans = sum(v*(v-1)//2 for v in Counter(l).values())

print(ans)