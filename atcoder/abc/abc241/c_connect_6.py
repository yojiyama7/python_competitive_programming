from itertools import product

N = int(input())
S = [input() for _ in range(N)]

def solve(cx, cy, dx, dy):
    wcnt = 0
    for k in range(6):
        x, y = cx+dx*k, cy+dy*k
        if not (0 <= x < N and 0 <= y < N):
            return False
        wcnt += (S[y][x] == '.')
    return (wcnt <= 2)

for cy, cx in product(range(N), repeat=2):
    for dy, dx in [(0, 1), (1, 0), (1, 1), (-1, 1)]:
        if solve(cx, cy, dx, dy):
            print("Yes")
            exit()
print("No")
