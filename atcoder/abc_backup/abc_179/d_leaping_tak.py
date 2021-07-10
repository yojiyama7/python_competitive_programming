# 点加算 区間合計 の Bit を 区間加算 点合計 の Bit として使える(差に注目する)

MOD = 998244353
# 1-indexed 閉区間 add_point sum_range MOD
class Bit:
    def __init__(self, n):
        self.n = n
        self.array = [0]*(n+1)
    
    def add(self, x, w=1):
        # print(f"{id(self)}: Bit.add({x}, {w})")
        while (x <= self.n):
            self.array[x] += w
            self.array[x] %= MOD
            x += (x & -x)
    
    def sum(self, x, y=None):
        # print(f"{id(self)}: Bit.sum({x}, {y})")
        if y == None:
            # 1~x
            sum_num = 0
            while (x > 0):
                sum_num += self.array[x]
                sum_num %= MOD
                x -= (x & -x)
            return sum_num
        else:
            # x~y
            return self.sum(y) - self.sum(x-1)

INF = float('inf')

N, K = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(K)]

dp = Bit(400010)
dp.add(1, 1)
dp.add(2, -1)
for i in range(1, N+1):
    for l, r in LR:
        dp.add(i+l, dp.sum(i))
        dp.add(i+r+1, -dp.sum(i))
    # print([dp.sum(j) for j in range(20)])

print(dp.sum(N))

################################

# # もうちょっと細かく詰めるbeki

# N, K = map(int, input().split())
# LR = [list(map(int, input().split())) for _ in range(K)]

# rngs = [(l, r+1) for l, r in LR]

# dp = [0]*N
# dp_acc = [0]*(N+1)
# dp[0] = 1
# dp_acc[0] = 1
# for i in range(1, N):
#     for rng in rngs:
#         l, r = max(0, i - rng[0]), max(0, i - rng[1])
#         print(l, r, dp_acc[r] - dp_acc[l])
#         dp[i] += dp_acc[r] - dp_acc[l]
#     dp_acc[i] = dp_acc[i-1] + dp[i]

# print(dp, dp_acc)

# print(dp[N-1])