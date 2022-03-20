N = int(input())
A = [list(map(int, input().split())) for _ in range(N-1)]

def solve_point(l):
    if len(l) < 2:
        return 0
    s = 0
    for i, x in enumerate(l):
        for j, y in enumerate(l):
            if i == j:
                continue
            if x < y:
                # print(x, y)
                s += A[x][y-x-1]
    return s

# 1グループ
max_num = solve_point(range(N))

# 2グループ
for i in range(2**N):
    g1, g2 = [], []
    for j in range(N):
        x = (i // 2**j) % 2
        if x == 1:
            g1.append(j)
        else:
            g2.append(j)
    m = solve_point(g1) + solve_point(g2)
    max_num = max(max_num, m)

for i in range(3**N):
    g1, g2, g3 = [], [], []
    for j in range(N):
        x = (i // 3**j) % 3
        if x == 1:
            g1.append(j)
        elif x == 2:
            g2.append(j)
        else:
            g3.append(j)
    m = solve_point(g1) + solve_point(g2) + solve_point(g3)
    max_num = max(max_num, m)

print(max_num)