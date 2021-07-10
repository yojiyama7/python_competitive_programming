
################################

# 桁dp っぽいなとは思ったし実装が浮かんでないこともないんですが
# 実装力と詰めの甘さ感ある
# 桁dp ちゃんと覚えてないとかけんな という気持ち
# 早解きで400位ぐらいだといいね
# AFTER CONTESET:
# コンテスト中の思考通り考えは良かった
# あまり時間的制約を気にせずに考えた際、詰めれるところを詰めておく
# あとでここ早くできそうだなーと思いながら、時間的な部分ではなく実装の詳細を思考する
# 辞書型(dict)使ってdpでも良さそう
# defaultdictって何だ -> (key, value) の value の型を制限する dict

# # RE

# from itertools import product

# N = input()

# abcd = [
#     None,
#     None,
#     (1, 0, 0, 0),
#     (0, 1, 0, 0),
#     (2, 0, 0, 0),
#     (0, 0, 1, 0),
#     (1, 1, 0, 0),
#     (0, 0, 0, 1),
#     (3, 0, 0, 0),
#     (0, 2, 0, 0),
# ]

# # dp(i, a, b, c, d, sm):
# # i桁目まで 2をa個, 3をb個, 5をc個, 7をd個 選んだ時の答え
# # ただし sm == 0 の時はi桁目がNと同じ
# # sm == 1 の時はi桁目がNより小さい
# dp = [[[[[[0 for sm in range(2)] for d in range(23)] for c in range(27)] for b in range(39)] for a in range(61)] for i in range(19)]
# dp[0][0][0][0][0][0] = 1

# # 遷移が重くなりすぎる気がする
# # 実装重くて疲れてきたマン
# for i in range(18):
#     Ni = int(N[i])
#     w, x, y, z = abcd[Ni]
#     for a, b, c, d in product(map(range, [61, 39, 27, 23])):
#         if a+w < 61 and b+x < 39 and c+y < 27 and d+z < 23:
#             dp[i+1][a+w][b+x][c+y][d+z][1] += dp[i][a][b][c][d][1]
#             dp[i+1][a+w][b+x][c+y][d+z][1] += dp[i][a][b][c][d][0]
#     dp[i+1][a+w][b+x][c+y][d+z][0] += dp[i][a][b][c][d][0]
#     for j in range(Ni):
#         dp[i+1][a][b][c][d][1] += dp[i][1][]
#     for a, b, c, d, sm in product(map(range, [61, 39, 27, 23, 2])):
#         dp[i+1][0 < Ni][0][0][0][0] += dp[i][sm[a][b][c][d]

#     # if Ni <= 1:
#     #     for a, b, c, d, sm in product(map(range, [61, 39, 27, 23, 2])):
#     #         dp[i+1][1 < Ni][a][b][c][d] += dp[i][sm][a][b][c][d]
#     # for j in range(2, Ni):
#     #     xa, xb, xc, xd = abcd[j]
#     #     for ya, yb, yc, yd in product(map(range, [61, 39, 27, 23])):
#     #         a, b, c, d = xa+ya, xb+yb, xc+yc, xd+yd
#     #         dp[i+1][1][a][b][c][d] += dp[i+1]
#     # for j in range(max(2, Ni), 10):
#     #     pass
