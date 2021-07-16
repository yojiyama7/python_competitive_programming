N, K = map(int, input().split())
A = list(map(int, input().split()))

# 山を構成する石の個数が i の時に手番の人は勝てるかどうか
dp = [0 for _ in range(K+1)]
dp[0] = False
for i in range(1, K+1):
    for a in A:
        if i-a < 0:
            continue
        if dp[i-a] == False:
            dp[i] = True

print("First" if dp[K] else "Second")
