# 1-indexed 閉区間 add_point sum_range
class Bit:
    def __init__(self, n):
        self.n = n
        self.array = [0]*(n+1)
        self.n_2 = 1
        while self.n_2*2 <= N:
            self.n_2 <<= 1

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

    def lower_bound(self, w):
        if w <= 0:
            return 0
        x = 0
        k = self.n_2
        while k > 0:
            if x + k <= self.n and self.array[x+k] < w:
                w -= self.array[x+k]
                x += k
            k >>= 1
        return x + 1

N, K = map(int, input().split())
P = list(map(int, input().split()))
# N = 5*10**5
# K = 1
# P = list(range(1, N+1))

bit = Bit(N)

for p in P[:K-1]:
    bit.add(p)
for i, p in enumerate(P[K-1:], start=K):
    bit.add(p)
    # print([bit.sum(i, i) for i in range(1, N+1)])
    print(bit.lower_bound(i-K+1))

