# https://atcoder.jp/contests/arc054/tasks/arc054_b

P = float(input())

# x年後に計算を開始した時の終了時刻: x + P/2**(x/1.5)
# 終了時刻を最小化したい

def f(x):
    if x >= 132:
        return x
    return x + P/2**(x/1.5)

ng, ok = -10**-9, P
while abs(f(ok)-f(ng)) > 10**-9:
    w = (ok-ng)/3
    if f(ng+w) < f(ng+2*w):
        ok = ng+2*w
    else:
        ng = ng+w

print(f(ok))
