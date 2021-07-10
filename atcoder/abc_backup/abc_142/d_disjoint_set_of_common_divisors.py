# もういいです死にます。
# 今日は参加しない方が良かったとか言っておきましょう
# 実は因数分解って素数一覧いらないっていうね
# 今日の気づき

import sys
sys.setrecursionlimit(10**8)

A, B = map(int, input().split())

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a%b)

g = gcd(A, B)
count = 0
for i in range(2, 10**6+3):
    if g%i == 0:
        count += 1
    while g%i == 0:
        g //= i
if g != 1:
    count += 1

print(count+1)
