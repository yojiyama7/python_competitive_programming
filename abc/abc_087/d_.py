N, M = map(int, input().split())
LRD = [list(map(int, input().split())) for _ in range(M)]

e = [[] for _ in range(N+1)]
for l, r, d in LRD:
    if l > r:
        l, r = r, l
        d *= -1
    e[l-1].append((r-1, d))
# print(e)

dp = [-1]*N
dp[0] = 0
for l, e_i in enumerate(e):
    for r, d in e_i:
        # print((l, r), d)
        if dp[r] in [-1, dp[l]+d]:
            dp[r] = dp[l]+d
        else:
            print("No")
            exit()

# print(dp)
print("Yes")