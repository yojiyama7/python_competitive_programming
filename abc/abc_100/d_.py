# 少ないパターンなら総当たれば良いという教訓
# 2**3 程度なら他のループを含めても結構いける

from itertools import product

INF = 10**18

N, M = map(int, input().split())
XYZ = [list(map(int, input().split())) for _ in range(N)]

# i番目までのケーキの内、j個食べた時のpointの最大値
# (ただしpointの計算時には、8通りのmaskを乗算する)

def mul_mask(l, mask):
    return [a*b for a, b in zip(l, mask)]

dp_std = [[-INF for _ in range(M+1)] for _ in range(N+1)]
for i in range(N+1):
    dp_std[i][0] = 0

max_p = -INF
masks = product([-1, 1], repeat=3)
for mask in masks:
    dp = dp_std[:]
    for i in range(1, N+1):
        score = sum(mul_mask(XYZ[i-1], mask))
        for j in range(1, M+1):
            dp[i][j] = max(
                dp[i-1][j],
                dp[i-1][j-1] + score
            )
            # for dp_i in dp:
            #     print(dp_i)
    p = dp[N][M]
    max_p = max(max_p, p)
    # print(p)

print(max_p)