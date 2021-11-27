# 公式解説
# Bi = Ai - i をしっていますか？　僕は知りませんでした

# 実装重かった
# 三分探索、尺取り法？、コスト計算、などにおいて不明な点が多すぎた

# [方針]
# 基本はD問題と同じようにするがidxをyがある場所に絞る <- いる？ <- いるかも
# ある範囲でのコストを求める必要がある 
## 範囲内の境界線を一つ選びそこに集合させるように移動するコストを考える
### 前処理O(N)でこの処理をO(1)にできる
# コストを f(x: 境界線) としたときに下に凸なので三分探索？
# min(f(x): x (l<=x<=r)) <= K のとき可能 -> 答えを更新する
 
# from itertools import accumulate as acc

# S = input()
# K = int(input())

# S_len = len(S)

# y_pos = [i for i, s in enumerate(S) if s == 'Y']
# y_len = len(y_pos)
# next_y_pos = dict((y_pos[i], y_pos[i+1]) for i in range(len(y_pos)-1))
# to_yidx = dict((y_pos_i, i) for i, y_pos_i in enumerate(y_pos))
# y_cnt_acc = [0] + list(acc(s == 'Y' for s in S))

# def calc_cost(l, r, mid):
#     lcost = (mid-1)*y_cnt_acc[mid] - 

# def calc_min_cost(l, r):
#     while True:
#         c1 = (l*2+r) // 3
#         c2 = (l+r*2) // 3
#         if c1 == c2:
#             break


#     return 0

# ans = 0
# r = y_pos[0]
# for yl, l in enumerate(y_pos):
#     r = max(l, r)
#     while to_yidx[r] < y_len and calc_min_cost(l, next_y_pos[r]) <= K:
#         r = next_y_pos[r]
#     ans = max(ans, to_yidx[r] - yl)

# print(ans)