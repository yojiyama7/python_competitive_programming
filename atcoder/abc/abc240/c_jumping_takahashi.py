N, X = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
dp = [set() for _ in range(N+1)]
dp[0].add(0)
for i in range(1, N+1):
    a, b = AB[i-1]
    for x in dp[i-1]:
        dp[i].add(x+a)
        dp[i].add(x+b)

if X in dp[N]:
    print("Yes")
else:
    print("No")