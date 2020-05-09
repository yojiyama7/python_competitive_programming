# 少ないときは総当たりゲーミング

N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
E = [list(map(int, input().split())) for _ in range(N)]

g = [[0]*C for _ in range(3)]
for y, e in enumerate(E):
    for x, e_i in enumerate(e):
        g[(x+y)%3][e_i-1] += 1
# print(g)

min_cost = 10**18
for c0 in range(C):
    for c1 in range(C):
        for c2 in range(C):
            if len({c0, c1, c2}) < 3:
                continue
            colors = [c0, c1, c2]
            # print(colors)
            cost = 0
            for i, g_i in enumerate(g):
                for j, g_j in enumerate(g_i):
                    # print(i, (j, colors[i]), D[j][colors[i]])
                    cost += D[j][colors[i]]*g_j
            min_cost = min(min_cost, cost)

print(min_cost)
