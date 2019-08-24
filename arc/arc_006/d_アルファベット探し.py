H, W = map(int, input().split(" "))
C = [input() for _ in range(H)]

shapes = [
    [
        "..o..",
        ".o.o.",
        "o...o",
        "ooooo",
        "o...o",
    ],
    [
        "oooo.",
        "o...o",
        "oooo.",
        "o...o",
        "oooo.",
    ],
    [
        ".ooo.",
        "o...o",
        "o....",
        "o...o",
        ".ooo."
    ],
]


def rotate(m):
    return ["".join(t) for t in zip(*m)][::-1]


# for l in rotate(["012345", "abcde", "o....", "o...o", ".ooo."]):
#     print(l)

def shape_type(m):
    for _ in range(4):
        for j in range(3):
            if m == shapes[j]:
                return j
        m = rotate(m)


# print(C[1][3])

ADS = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

counts = [0, 0, 0]

visited = [[False for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if C[i][j] == ".":
            continue
        if visited[i][j]:
            continue
        visited[i][j] = True
        # print((i, j), visited)
        min_x, max_x = j, j
        min_y, max_y = i, i
        # print((min_x, min_y), (max_x, max_y))
        q = [(j, i)]
        while q:
            # print(q)
            this_pos = this_x, this_y = q.pop()
            # print(this_pos, C[this_y][this_x])
            # print(min(min_x, this_x), max(max_x, this_x))
            # print(min(min_y, this_y), max(max_y, this_y))
            # min_x, max_x = min(min_x, this_x), max(max_x, this_x)
            # min_y, max_y = min(min_y, this_y), max(max_y, this_y)
            # print(this_pos, min_y)

            # print((this_x, this_y))
            for ad_x, ad_y in ADS:
                pos = x, y = this_x+ad_x, this_y+ad_y
                # print(pos)
                if not (0 <= x < W and 0 <= y < H):
                    continue
                if C[y][x] == ".":
                    continue
                if visited[y][x]:
                    continue
                # print("tttt", pos)
                visited[y][x] = True
                # print(pos)
                min_x, max_x = min(min_x, x), max(max_x, x)
                min_y, max_y = min(min_y, y), max(max_y, y)
                # print((x, y), visited)
                q.append(pos)
        # for v in visited:
        #     print("".join(".#"[v_i] for v_i in v))
        print((min_x, min_y), (max_x, max_y))
        step = (max_y-min_y+1)//5
        print(step)
        # ad = (step+1)//2
        shape = []
        for y in range(min_y, max_y+1, step):
            t = ""
            for x in range(min_x, max_x+1, step):
                t += C[y][x]
            shape.append(t)
        counts[shape_type(shape)] += 1
        # for s in shape:
        #     print(s)

print(*counts)
