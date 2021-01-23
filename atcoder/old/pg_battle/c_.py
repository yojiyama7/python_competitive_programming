# 座標系を x+y, x-y で変換して (同じマンハッタン距離を持つものを正方形に並べるため)
    # というか、なぜ(x+y, x-y)にするのか、他の要素に影響を与えそうだからダメかも？)
    # (ちなみにこれx, yの範囲が決まっていたらどうなる、、)
# 累積和すれば良い(ダメそう)
# がどちらも慣れておらずpythonで計算量がどのくらいになるか
# どの実装なら通るか、PyPyで使えないものはないかなど
# わからず書けなかった。無念。
# 少なくとも書けてはなかった。

import numpy as np

N = int(input())
XYD = [list(map(int, input().split())) for _ in range(N)]

m = np.zeros((6001, 6001))
for x, y, d in XYD:
    m[3000+x+y][3000+x-y] += 1

m = np.cumsum(m, axis=1)
m = np.cumsum(m, axis=0)

print(m)

def fetch_count(pos1, pos2):
    x1, y1 = pos1
    a1, b1 = x1+y1, x1-y1
    x2, y2 = pos2
    a2, b2 = x2+y2, x2-y2
    return m[a2][]
 
# print(fetch_count((1, 1), (1, 1)))

