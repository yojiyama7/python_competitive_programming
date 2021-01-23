# 方向ごとに分割して考える累積和
# 基本はDP これをみてDPだと考えるほうが色々な問題に対応できそう
# 3方向ごとの累積和 + 全ての方向からの合計を表す1つ の合計4つのテーブルを管理する
# 遷移が y, y-1 の2つの行のみを参照するので各テーブルの大きさを W にでき空間計算量を O(W) にできる

################################

MOD = 10**9+7

H, W = map(int, input().split())
S = [input() for _ in range(H)]

dp = [[0 for _ in range(W)] for _ in range(H)]
dp[0][0] = 1
# to_right, to_rightdown, to_down
tables = [[[0 for _ in range(W)] for _ in range(H)] for _ in range(3)]

for y in range(H):
    for x in range(W):
        if S[y][x] == "#" or x == y == 0:
            continue
        if x >= 1:
            # 右への経路が何通りか = nマス左から飛んでここへ(走) + 1マス左からここへ(歩)
            tables[0][y][x] = (tables[0][y][x-1] + dp[y][x-1]) % MOD
        if x >= 1 and y >= 1:
            tables[1][y][x] = (tables[1][y-1][x-1] + dp[y-1][x-1]) % MOD
        if y >= 1:
            tables[2][y][x] = (tables[2][y-1][x] + dp[y-1][x]) % MOD
        dp[y][x] = sum(t[y][x] for t in tables) % MOD

# list(map(print, dp))

print(dp[H-1][W-1])

################################

# # WA

# MOD = 10**9+7

# H, W = map(int, input().split())
# S = [input() for _ in range(H)]

# to_right = [[0 for _ in range(W)] for _ in range(H)]
# to_rightdown = [[0 for _ in range(W)] for _ in range(H)]
# to_down = [[0 for _ in range(W)] for _ in range(H)]

# to_right[0][0] = 1
# # to_rightdown[0][0] = 1
# # to_down[0][0] = 1
# all_map = [to_right, to_rightdown, to_down]

# for y in range(H):
#     for x in range(W):
#         if S[y][x] == "#":
#             continue
#         if x >= 1:
#             to_right[y][x] = sum(m[y][x-1] for m in all_map) % MOD
#         if y >= 1:
#             to_down[y][x] = sum(m[y-1][x] for m in all_map) % MOD
#         if x >= 1 and y >= 1:
#             to_rightdown[y][x] = sum(m[y-1][x-1] for m in all_map) % MOD

# for m in all_map:
#     [print(m_i) for m_i in m]
#     print("---")

# result = sum(m[H-1][W-1] for m in all_map)
# print(result)