# DPの線を狙ったのはよし、確率DPを学べ
# dp[100][*][*], dp[*][100][*], dp[*][*][100] を 0 とするのが肝
# いまいち期待値というものに対して納得感がない

A, B, C = map(int, input().split())

# dp[i][j][k] = Aがi枚, Bがj枚, Cがk枚 から いずれかが100になるまでの操作回数の期待値
dp = [[[-1 for _ in range(101)] for _ in range(101)] for _ in range(101)]
def solve(a, b, c):
    if 100 in [a, b, c]:
        return 0
    if dp[a][b][c] == -1:
        coin_sum = a+b+c
        l = [
            a/coin_sum * (solve(a+1, b, c) + 1),
            b/coin_sum * (solve(a, b+1, c) + 1),
            c/coin_sum * (solve(a, b, c+1) + 1),
        ]
        # print((a,b,c), l)
        dp[a][b][c] = sum(l)
    return dp[a][b][c]

print(solve(A, B, C))