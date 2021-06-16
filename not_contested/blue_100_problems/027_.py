# https://atcoder.jp/contests/joi2009yo/tasks/joi2009yo_d

from itertools import product

M = int(input())
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]
def solve(cx, cy):
    if not (0 <= cx < M and 0 <= cy < N):
        return 0
    if A[cy][cx] == 0:
        return 0
    if visited[cy][cx]:
        return 0
    visited[cy][cx] = 1
    ans = 0
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        x, y = cx+dx, cy+dy
        score = solve(x, y) + 1
        ans = max(score, ans)
    visited[cy][cx] = 0
    return ans

ans = 0
for y, x in product(range(N), range(M)):
    score = solve(x, y)
    ans = max(score, ans)

print(ans)