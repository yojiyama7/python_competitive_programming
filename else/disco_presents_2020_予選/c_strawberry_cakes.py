# 横に取れるだけ取っていちごの無い行があれば上か下からコピペ
H, W, K = map(int, input().split())
S = [input() for _ in range(H)]

group = [[0 for _ in range(W)] for _ in range(H)]
group_num = 1

for y in range(H):
    for x in range(W):
        if S[y][x] == ".":
            continue
        group[y][x] = group_num
        for r in [(x-1, -1, -1), (x+1, W)]:
            for x2 in range(*r):
                if S[y][x2] == "#":
                    break
                group[y][x2] = group_num
        group_num += 1

for y in range(H):
    if group[y][0] == 0:
        continue
    for r in [(y-1, -1, -1), (y+1, H)]:
        for y2 in range(*r):
            if group[y2][0] > 0:
                break
            group[y2] = group[y]

for l in group:
    print(*l)

################################

# H, W, K = map(int, input().split())
# S = [input() for _ in range(H)]

# group = [[0 for _ in range(W)] for _ in range(H)]

# group_num = 1
# for y in range(H):
#     for x in range(W):
#         if S[y][x] == ".":
#             continue
#         group[y][x] = group_num

#         min_x2 = 0
#         for x2 in range(x-1, -1, -1):
#             if S[y][x2] == "#" or group[y][x2] > 0:
#                 min_x2 = x2
#                 break
#             group[y][x2] = group_num
#         max_x2 = W-1
#         for x2 in range(x+1, W):
#             if S[y][x2] == "#" or group[y][x2] > 0:
#                 max_x2 = x2
#                 break
#             group[y][x2] = group_num
#         for y2 in range(y-1, -1, -1):
#             if "#" in S[y2][min_x2:max_x2+1] or any(group[y2][min_x2:max_x2+1]):
#                 break
#             for x2 in range(min_x2, max_x2+1):
#                 group[y2][x2] = group_num
#         for y2 in range(y+1, H):
#             if "#" in S[y2][min_x2:max_x2+1] or any(group[y2][min_x2:max_x2+1]):
#                 break
#             for x2 in range(min_x2, max_x2+1):
#                 group[y2][x2] = group_num
        
#         for l in group:
#             print(*l)

#         group_num += 1

# for l in group:
#     print(*l)