MOD = 10**9+7

S = input()

n = len(S)

none = 1
c = 0
ch = 0
cho = 0
chok = 0
choku = 0
chokud = 0
chokuda = 0
chokudai = 0

for s in S:
    if s == 'c':
        c += none
        c %= MOD
    elif s == 'h':
        ch += c
        ch %= MOD
    elif s == 'o':
        cho += ch
        cho %= MOD
    elif s == 'k':
        chok += cho
        chok %= MOD
    elif s == 'u':
        choku += chok
        choku %= MOD
    elif s == 'd':
        chokud += choku
        chokud %= MOD
    elif s == 'a':
        chokuda += chokud
        chokuda %= MOD
    elif s == 'i':
        chokudai += chokuda
        chokudai %= MOD

print(chokudai)

################################

MOD = 10**9+7

S = input()

n = len(S)

# Sのi文字目まででchokudaiのj文字目までを完成させれる通り数
dp = [[0 for _ in range(9)] for _ in range(n+1)]
dp[0][0] = 1
for i, s in enumerate(S):
    for j in range(9):
        dp[i+1][j] = dp[i][j]
    for j, c in enumerate("chokudai", start=1):
        if s == c:
            dp[i+1][j] += dp[i][j-1]
            dp[i+1][j] %= MOD

print(dp[n][8])

