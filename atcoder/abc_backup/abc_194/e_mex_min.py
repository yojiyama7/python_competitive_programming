# 色々解き方がありますねの回
# たぶん必要以上に複雑にした

from itertools import chain

INF = float('inf')

# 1-indexed 閉区間
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

N, M = map(int, input().split())
A = list(map(int, input().split()))

A = [a+1 for a in A]
# print("A:", A)

bit_cnt = Bit(1500010)
bit_flag = Bit(1500010)
for a in A[:M]:
    bit_cnt.add(a)
    if bit_cnt.sum(a, a) == 1:
        bit_flag.add(a)

def mex():
    ok = 0
    ng = 1500010
    while abs(ok - ng) > 1:
        mid = (ok+ng)//2
        # print(ok, mid, ng, end="")
        if bit_flag.sum(mid) == mid:
            ok = mid
            # print(": ok")
        else:
            ng = mid
            # print(": ng")
    return ok

min_num = mex()
# print([[bit.sum(i, i) for i in range(10)] for bit in [bit_cnt, bit_flag]])
for i in range(N-M):
    bit_cnt.add(A[i], -1)
    if bit_cnt.sum(A[i], A[i]) == 0:
        bit_flag.add(A[i], -1)
    bit_cnt.add(A[M+i])
    if bit_cnt.sum(A[M+i], A[M+i]) == 1:
        bit_flag.add(A[M+i])
    # print([[bit.sum(i, i) for i in range(10)] for bit in [bit_cnt, bit_flag]])
    min_num = min(min_num, mex())

print(min_num)

################################

# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# N, M = 1500000, 1500
# A = [1]*N
# A = list(chain(*[range(1500) for _ in range(1000)]))
# for i in range(0, N, 8332):
#     print(i)
#     A[i] = 10000
# print(len(A))

# def mex(l):
#     cnt = [0]*2000000
#     for l_i in l:
#         cnt[l_i] += 1
#     i = 0
#     while cnt[i]:
#         i+=1
#     return i

# l = [0]*2000000
# for a in A[:M]:
#     l[a] += 1
# mex_val = 0
# while l[mex_val]:
#     mex_val += 1

# min_num = mex_val
# for i in range(N-M):
#     # print(M, i)
#     # print(A[M+i])
#     l[A[M+i]] += 1
#     while l[mex_val]:
#         mex_val += 1
#     l[A[i]] -= 1
#     if A[i] < mex_val and l[A[i]] == 0:
#         mex_val = A[i]
#     min_num = min(min_num, mex_val)

# print(min_num)