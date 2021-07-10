# 脳みそ死んだ無理ぽ

# 遷移間に合わないなと考えていたら
# 遷移最適化のためのメモを用意することでできるらしい
# 何をメモしたいん
# メモをしやすくするためにdpの形も少し変える？
# ようわからんなってきた

from itertools import accumulate as acc
from collections import Counter

MOD = 10**9+7

N = int(input())
A = list(map(int, input().split()))

A_acc = [0] + list(acc(A))

# dp[i]: i番目までの要素でjグループに分けるパターン数
dp = [[0 for j in range(N+1)] for i in range(N+1)]
dp[0][0] = 1
memo = [[0 for j in range(N+1)] for i in range(N+1)]

for i in range(N):
    for j in range(N):
        dp[i+1][j+1] = dp[i]