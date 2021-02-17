H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(10)]
A = [list(map(int, input().split())) for _ in range(H)]

dist = [[INF for _ in range(10)] for _ in range(10)]
for s in range(10):
	

################################

# ワーシャルフロイド法などで最短経路探索もあり。
# dijkstraもありか、scipy(サイパイ)すごそう。
# 最短経路むずい。

################################

# from itertools import permutations as per

# H, W = map(int, input().split())
# C = [list(map(int, input().split())) for _ in range(10)]
# A = [list(map(int, input().split())) for _ in range(H)]

# これが俗にいうbitDPでは、、？
# dp[i(1<<10)][j(10)][k(10)] = jからi(bit flags)を通ってkにできる最小コスト
# 疲れた。

# dp = [[[10**18 for _ in range(10)] for _ in range(10)] for _ in range(1<<10)]
# dp 
# for j in range(10):
#     for k in range(10):
