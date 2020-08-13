H, W, K = map(int, input().split())

def swap(l, a, b):
    # print("s", a, b)
    l[a], l[b] = l[b], l[a]

def check_row(m):
    l = list(range(W))
    b = 0
    for i in range(W-1):
        c = (m>>i)%2
        # print(b, c)
        if b == c == 1:
            return False
        if c == 1:
            swap(l, i, i+1)
        b = c
    return l


# i行目までで1がjにいる組み合わせの数
dp = [[0 for j in range(W)] for i in range(H+1)]
dp[0][0] = 1

for i in range(1, H+1):
    for j in range(1<<(W-1)):
        r = check_row(j)
        if r == False:
            continue
        # print(r)
        for k, r_i in enumerate(r):
            # print(i, k, r_i)
            dp[i][r_i] = (dp[i][r_i] + dp[i-1][k]) % (10**9+7)

# print(*dp, sep="\n")
print(dp[H][K-1])


