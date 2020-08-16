# ARC 029 A - 高橋君とお肉
# https://atcoder.jp/contests/arc029/tasks/arc029_1

N = int(input())
T = [int(input()) for _ in range(N)]

min_cost = 10**18
for i in range(1<<N):
    ab = [0, 0]
    for j in range(N):
        ab[(i>>j)%2] += T[j]
    cost = max(ab)
    min_cost = min(min_cost, cost)

print(min_cost)