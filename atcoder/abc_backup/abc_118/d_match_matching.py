MINUS_INF = "-"
MATCHES = [-1, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def char_max(a, b):
    if a == MINUS_INF:
        return b
    la, lb = len(a), len(b)
    if la < lb:
        return b
    elif la == lb and a < b:
        return b
    return a


N, M = map(int, input().split())
A = input().split()

dp = [MINUS_INF]*(10**4+10)
dp[0] = ""
for i in range(N+1):
    if dp[i] == MINUS_INF:
        continue
    for a in A:
        # 配るdp?
        dp[i+MATCHES[int(a)]] = char_max(
            dp[i+MATCHES[int(a)]],
            dp[i] + a
        )

print(dp[N])