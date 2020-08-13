from bisect import bisect_left

BIG_NUM = 10**9

n = int(input())
w = [int(input()) for _ in range(n)]

l = [BIG_NUM] * n
for w_i in w:
    [bisect_left(l, w_i)] = w_i

print(bisect_left(l, BIG_NUM))
