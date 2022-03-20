# 3 要素の等差数列は (A, B, C) は 2B - A - C = 0 と同値
# 数学しようねの気持ち
# 問題文の式変形したらすぐ気づけるからね

# 数学は偉大()

A1, A2, A3 = map(int, input().split())

p = A2*2 - A1 - A3

cost = 0
if p < 0:
    cnt = -(-abs(p)//2)
    p += 2*cnt
    cost += cnt

cost += p

print(cost)