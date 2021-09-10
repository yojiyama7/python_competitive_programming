H, W = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0
for i in range(H):
    for j in range(W):
        if j+1 < W and S[i][j] == S[i][j+1] == '.':
            ans += 1
        if i+1 < H and S[i][j] == S[i+1][j] == '.':
            ans += 1

print(ans)