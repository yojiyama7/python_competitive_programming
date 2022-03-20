from collections import deque

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]
# H, W = 80, 80
# A = [[1]*80]*80
# B = [[4]*80]*80

c = [[abs(A[i][j] - B[i][j]) for j in range(W)] for i in range(H)]


# [print(c_i) for c_i in c]

dp = [[[0 for _ in range(170)] for _ in range(W)] for _ in range(H)]
dp[0][0][c[0][0]] = 1

v = [[0 for _ in range(W)] for _ in range(H)]
v[0][0] = 1
q = deque([(0, 0)])
while q:
    tx, ty = q.popleft()
    tdp = dp[ty][tx]

    # print(tx, ty)
    for dx, dy in [(0, 1), (1, 0)]:
        nx, ny = tx+dx, ty+dy
        if not (0 <= nx < W and 0 <= ny < H):
            continue
        nc = c[ny][nx]
        for i, m in enumerate(tdp):
            if m == 0:
                continue
            if abs(i-nc) <= 160:
                dp[ny][nx][abs(i-nc)] = 1
            if abs(i+nc) <= 160:
                dp[ny][nx][abs(i+nc)] = 1
        print((nx, ny), nc, dp[ny][nx])
        
        if v:
            continue
        q.append((nx, ny))
        v[ny][nx] = 1
        # print((tx, ty), (nx, ny))

[[print(j, i, dp_j) for j, dp_j in enumerate(dp_i)] for i, dp_i in enumerate(dp)]

print(dp[H-1][W-1].index(1))
        




