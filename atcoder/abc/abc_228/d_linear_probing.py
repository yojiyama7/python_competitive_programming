# この実装だと既に追加してある範囲の左側に要素を書き込むとバグる
# 連続する部分を塊としてとらえるような実装が良い(両端をまたいで連続する可能性に注意する)

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
    def add0idx(self, x, w=1):
        self.add(x+1, w)

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
    def sum0idx(self, x, y=None):
        return self.sum(x+1, None if y == None else y+1)

Q = int(input())
TX = [list(map(int, input().split())) for _ in range(Q)]

N = 1<<20
a = [-1]*N
# 0 ~ N
next_empty = Bit(N+1)

for t, x in TX:
    if t == 1:
        h = x%N
        empty = h + next_empty.sum0idx(h)
        a[empty] = x
        if x%N == N-1:
            continue
        if empty < N:
            next_empty.add0idx(h, 1)
            next_empty.add0idx(empty+1, -1)
        else:
            empty %= N
            next_empty.add0idx(h, 1)
            next_empty.add0idx(0, 1)
            next_empty.add0idx(empty+1, -1)
    else:
        ans = a[x%N]
        print(ans)
    # print([next_empty.sum0idx(i) for i in range(N)], a)
