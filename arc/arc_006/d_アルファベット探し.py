H, W = map(int, input().split(" "))
C = [input() for _ in range(H)]

ADS = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

counts = [0, 0, 0, 0]

visited = [[False for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if C[i][j] == ".":
            continue
        if visited[i][j]:
            continue
        visited[i][j] = True

        min_x, max_x = j, j
        min_y, max_y = i, i
        black_count = 1
        q = [(j, i)]
        while q:
            this_pos = this_x, this_y = q.pop()

            for ad_x, ad_y in ADS:
                pos = x, y = this_x+ad_x, this_y+ad_y
                if not (0 <= x < W and 0 <= y < H):
                    continue
                if C[y][x] == ".":
                    continue
                if visited[y][x]:
                    continue
                visited[y][x] = True
                black_count += 1
                min_x, max_x = min(min_x, x), max(max_x, x)
                min_y, max_y = min(min_y, y), max(max_y, y)
                q.append(pos)

        times = (max_y-min_y+1)//5
        t = [12, 16, 11].index(black_count // (times**2))
        counts[t] += 1

print(*counts[:3])
