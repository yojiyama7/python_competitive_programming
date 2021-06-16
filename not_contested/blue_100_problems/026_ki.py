# https://atcoder.jp/contests/abc138/tasks/abc138_d

import sys
sys.setrecursionlimit(10**8)

N, Q = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N-1)]
PX = [list(map(int, input().split())) for _ in range(Q)]


g = [set() for _ in range(N)]
parent = [None]*N
for a, b in AB:
    a -= 1
    b -= 1
    g[a].add(b)
    parent[b] = a

score = [0]*N
for p, x in PX:
    p -= 1
    score[p] += x

# print(score, parent)

calced_score = [None]*N
def dfs(i):
    parent_calced_score = calced_score[parent[i]] if parent[i] != None else 0
    # print(i, calced_score, score[i])
    calced_score[i] = parent_calced_score + score[i]

    for to in g[i]:
        dfs(to)

dfs(0)

print(*calced_score)
