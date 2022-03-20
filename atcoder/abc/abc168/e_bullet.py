# 最後の詰めがむずい

from collections import Counter

MOD = 10**9+7

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

# A[i]*A[j] + B[i]*B[j] = 0
# A[i]*A[j] = -B[i]*B[j]
# A[i] = -B[i]*B[j]/A[j]
# A[i]/B[i] = -B[j]/A[j]

# i == j の時
# A[i]/B[i] = -B[i]/A[i]
# a/b = -b/a
# a = -b * b / a
# a**2 = -b**2
# (a**2 => 0), (-b**2 <= 0) なので成り立たない

P = [a/b for a, b in AB]
Q = [-b/a for a, b in AB]



