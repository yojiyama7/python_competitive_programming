# 最長が欲しいなら尺取り法で良さそう

# 1-indexed 閉区間 add_point sum_range
class Bit:
    def __init__(self, n):
        self.n = n
        self.array = [0]*(n+1)

    def add(self, x, w=1):
        # print(f"{id(self)}: Bit.add({x}, {w})")
        while (x <= self.n):
            self.array[x] += w
            x += (x & -x)

    def sum(self, x, y=None):
        # print(f"{id(self)}: Bit.sum({x}, {y})")
        if y == None:
            # 1~x
            sum_num = 0
            while (x > 0):
                sum_num += self.array[x]
                x -= (x & -x)
            return sum_num
        else:
            # x~y
            return self.sum(y) - self.sum(x-1)

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
d = dict()
l = Bit(N)
for r, a in enumerate(A, start=1):
    if a in d:
        l.add(d[a], -1)
    d[a] = r
    l.add(r, 1)
    ok, ng = r, 0
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if l.sum(mid, r) <= K:
            ok = mid
        else:
            ng = mid
    # print([ok, r], A[ok-1:r], K)
    # [ok, r] の長さ
    score = r - ok + 1
    ans = max(ans, score)

print(ans)
