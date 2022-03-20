# ARC 037 B バウムテスト
# https://atcoder.jp/contests/arc037/submissions/me

N, M = map(int, input().split())
UV = [list(map(int, input().split())) for _ in range(M)]

d = [set() for _ in range(N)]
for u, v in UV:
    d[u-1].add(v-1)
    d[v-1].add(u-1)

visited = set()

def dfs(x):
    if x in visited:
        return False
    visited.add(x)
    r = True
    for d_i in d[x]-visited:
        if dfs(d_i) == False:
            r = False
    return r

count = 0
for i in range(N):
    if i in visited:
        continue
    # print(visited)
    if dfs(i):
        count += 1

print(count)