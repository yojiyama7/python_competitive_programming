# gcd(a, b) == 1 なら a, b に辺を張る
# カードの集合をSとして S が完全グラフの時この組み合わせは可能
# カード全体を A として A に含まれる完全グラフの個数
# 

A, B = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    return (b, a%b)

ans = 2**(B-A+1)
print(ans)
for i in range(A, B+1):
    for j in range(A, B+1):
        if i == j:
            continue
        if gcd(i, j) != 1:
            pass