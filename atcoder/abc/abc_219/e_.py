from itertools import chain

A = [list(map(int, input().split())) for _ in range(4)]

def is_connected(m):
    fx, fy = -1, -1
    for i in range(4):
        for j in range(4):
            if m[i][j]:
                fy = i
                fx = j
                break
    visited = [[0 for j in range(4)] for i in range(4)]
    visited[fy][fx] = 1
    q = [(fx, fy)]
    while q:
        tx, ty = q.pop()

        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            x, y = tx+dx, ty+dy
            if not (0 <= x < 4 and 0 <= y < 4):
                continue
            if m[y][x] == 0:
                continue
            if visited[y][x]:
                continue
            visited[y][x] = 1
            q.append((x, y))
    ans = True
    for i in range(4):
        for j in range(4):
            if m[i][j] == visited[i][j]:
                continue
            ans = False
            break
    return ans

def is_connected2(m):
    m = [[0 for _ in range(6)]] + [[0]+mi+[0] for mi in m] + [[0 for _ in range(6)]]
    # print(m)
    fx, fy = 0, 0
    visited = [[0 for j in range(6)] for i in range(6)]
    visited[fy][fx] = 1
    q = [(fx, fy)]
    while q:
        tx, ty = q.pop()

        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            x, y = tx+dx, ty+dy
            if not (0 <= x < 6 and 0 <= y < 6):
                continue
            if m[y][x] == 1:
                continue
            if visited[y][x]:
                continue
            visited[y][x] = 1
            q.append((x, y))
    ans = True
    for i in range(6):
        for j in range(6):
            if m[i][j] != visited[i][j]:
                continue
            ans = False
            break
    return ans

all_vil = sum(chain(*A))
# print(all_vil)
# cnt = 0
ans = 0
for i in range(1<<16):
    vil = 0
    m = [[0 for _ in range(4)] for _ in range(4)]
    for j in range(16):
        x, y = j%4, j//4
        if (i>>j)&1:
            m[y][x] = 1
            vil += A[y][x]
    if vil < all_vil:
        continue
    if is_connected(m) and is_connected2(m):
        # print(m)
        # if cnt < 4:
            # [print(mi) for mi in m]
            # cnt += 1
        ans += 1

print(ans)