# 桁DP?　NO
# bit DP?

ENUM = enumerate

N, X = map(int, input().split())
A = list(map(int, input().split()))
# N, X = 15, 10**6
# A = [2**i for i in range(N)]

def f(x):
    flag = 0
    for i, a in ENUM(reversed(A)):
        if x >= a:
            x %= a
            flag |= 1<<i
        if x == 0:
            break
    return flag

print(X, bin(f(X)))
y = X
while (True):
    if not f(y) & f(y-X):
        print(y, bin(f(y))[2:], bin(f(y-X))[2:])
    y += 1
