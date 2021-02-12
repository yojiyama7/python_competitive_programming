H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

idx = 0
m = [[-1 for _ in range(W)]for _ in range(H)]
for y in range(H):
    for x in range(W):
        if A[idx] == 0:
            idx += 1
        m[y][-(x+1) if y%2 else x] = idx+1
        A[idx] -= 1

[print(*m_i) for m_i in m]
