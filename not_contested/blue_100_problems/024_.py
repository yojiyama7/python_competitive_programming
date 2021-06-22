# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B

N = int(input())
U = [list(map(int, input().split())) for _ in range(N)]

g = [None] + [u[2:] for u in sorted(U)]

in_time = [None]*(N+1)
out_time = [None]*(N+1)

time = 1
def dfs(x):
    global time
    if in_time[x]:
        return
    in_time[x] = time
    time += 1
    for to in g[x]:
        dfs(to)
    out_time[x] = time
    time += 1

for i in range(1, N+1):
    dfs(i)
for i in range(1, N+1):
    print(i, in_time[i], out_time[i])
