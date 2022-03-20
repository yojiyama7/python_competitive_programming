from itertools import permutations as permu

INF = 10**18

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
XY = [list(map(int, input().split())) for _ in range(M)]

invalids = set()
for x, y in XY:
    x -= 1
    y -= 1
    invalids.add((x, y))
    invalids.add((y, x))

def solve_cost(l):
    ans = 0
    for i in range(N):
        if i+1 < N:
            ab = (l[i], l[i+1])
            if ab in invalids:
                return INF
        ans += A[l[i]][i]
    return ans

ans = INF
for l in permu(range(N)):
    score = solve_cost(l)
    # print(l, score)
    ans = min(ans, score)
if ans == INF:
    print(-1)
else:
    print(ans)
