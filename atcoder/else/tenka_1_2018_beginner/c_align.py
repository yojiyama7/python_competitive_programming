# 案外むずい問題多くないか

N = int(input())
A = [int(input()) for _ in range(N)]

A.sort()

# 各要素について倍率を考える 各要素ごとに影響を考える
# p1 > p2 < p3 ... の場合
multi = [[1, -1][i%2] * (1 + (0 < i < N-1)) for i in range(N)]
ans = sum(a*m for a, m in zip(A, sorted(multi)))

multi = [-m for m in multi]
ans = max(
    ans,
    sum(a*m for a, m in zip(A, sorted(multi)))
)

print(ans)

################################

# N = int(input())
# A = [int(input()) for _ in range(N)]

# A.sort()

# l = [-1]*N
# for i, a in enumerate(A):
#     x = i*2
#     if x >= N:
#         x %= N
#         x += (N%2 == 0)
#     l[x] = a

# print(l)

# print(sum([abs(l[i] - l[i-1]) for i in range(N-1)]))