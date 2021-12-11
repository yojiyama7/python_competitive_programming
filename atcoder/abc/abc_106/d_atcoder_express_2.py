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

from itertools import accumulate as acc

N, M, Q = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(M)]
PQ = [tuple(map(int, input().split())) for _ in range(Q)]

Q_P = dict((i, set()) for i in range(1, N+1))
for p, q in PQ:
    Q_P[q].add(p)
R_L = dict((i, []) for i in range(1, N+1))
for l, r in LR:
    R_L[r].append(l)
part = Bit(N)
ans_dict = dict()
cnt = 0
# print(R_L, Q_P)
for r in range(1, N+1):
    cnt += len(R_L[r])
    for l in R_L[r]:
        part.add(l)
    # print([part.sum(i) for i in range(1, N+1)])
    for l in Q_P[r]:
        # print(l, part.sum(l-1))
        ans = cnt - part.sum(l-1)
        ans_dict[(l, r)] = ans
    # print(r, "cnt: ", cnt)

# print(ans_dict)

for p, q in PQ:
    print(ans_dict[(p, q)])