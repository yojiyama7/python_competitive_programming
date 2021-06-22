# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C&lang=ja

Q = int(input())

def lcs(a, b):
    n, m = len(a), len(b)

    # Yのi文字目までつくれるLCS (1-idx)
    dp = [0 for _ in range(m+1)]
    for i in range(1, n+1):
        mem = dp[:]
        x = a[i-1] # 文字列参照を変数に入れただけで通るのマジで
        for j in range(1, m+1):
            # 定数倍の鬼
            if x == b[j-1]:
                dp[j] = mem[j-1] + 1
            elif dp[j] < dp[j-1]:
                dp[j] = dp[j-1]
    # list(map(print, dp))
    return dp[m]

ans_list = []
for _ in range(Q):
    X = input()
    Y = input()

    ans_list.append(lcs(X, Y))
    # X, Y = list(map(ord, X)), list(map(ord, Y))

print(*ans_list, sep='\n')
