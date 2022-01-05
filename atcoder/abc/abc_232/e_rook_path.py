MOD = 998244353

H, W, K = map(int, input().split())
X1, Y1, X2, Y2 = map(int, input().split())

acnt, bcnt, ccnt, dcnt = 1, W-1, H-1, (W-1)*(H-1)
a, b, c, d = [1, 0, 0, 0]
for _ in range(1, K+1):
    na = b*bcnt + c*ccnt
    nb = d*(H-1) + b*(bcnt-1) + a
    nc = d*(W-1) + c*(ccnt-1) + a
    nd = d*(W-2 + H-2) + b + c
    a, b, c, d = na%MOD, nb%MOD, nc%MOD, nd%MOD
xeq = (X1 == X2)
yeq = (Y1 == Y2)
if xeq and yeq:
    print(a)
elif yeq:
    print(b)
elif xeq:
    print(c)
else:
    print(d)

################################

# MOD = 998244353

# H, W, K = map(int, input().split())
# X1, Y1, X2, Y2 = map(int, input().split())

# b0 = 1
# b1w = 0
# b1h = 0
# b2 = 0
# s0, s1w, s1h, s2 = None, None, None, None
# for _ in range(K):
#     s0 = b1w*(W-1) + b1h*(H-1)
#     s0 %= MOD
#     s1w = b0 + b1w*(W-2) + b2*(H-1)
#     s1w %= MOD
#     s1h = b0 + b1h*(H-2) + b2*(W-1)
#     s1h %= MOD
#     s2 = b1w + b1h + b2*(H+W-4)
#     s2 %= MOD
#     b0, b1w, b1h, b2 = s0, s1w, s1h, s2

# if (X1 == X2) and (Y1 == Y2):
#     print(s0)
# elif (X1 == X2):
#     print(s1h)
# elif (Y1 == Y2):
#     print(s1w)
# else:
#     print(s2)
