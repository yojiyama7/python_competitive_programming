# 関数合成？
# 下限、上限、足す値、をそれぞれ管理して
# 全ての関数を先に合成して
# それをXに適応する
# なぜACなのかいまいちわかっていない

INF = float('inf')

N = int(input())
AT = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
X = list(map(int, input().split()))

low, high = -INF, INF
add = 0
for a, t in AT:
    if t == 1:
        low += a
        high += a
        add += a
    elif t == 2:
        low = max(low, a)
        high = max(high, a)
    else:
        low = min(low, a)
        high = min(high, a)

for x in X:
    m = (x + add)
    m = max(low, m)
    m = min(high, m)
    print(m)
