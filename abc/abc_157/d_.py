N, M, K = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]
CD = [list(map(int, input().split())) for _ in range(K)]

friend_or_block = [[0]*N for _ in range(N)]
for a, b in AB:
    a, b = a-1, b-1
    friend_or_block[a][b] = 1
    friend_or_block[b][a] = 1
for c, d in CD:
    c, d = c-1, d-1
    friend_or_block[c][d] = 1
    friend_or_block[d][c] = 1

