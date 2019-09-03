from bisect import bisect

INF = 10**24

A, B, Q = map(int, input().split())
S, T, X = [[int(input()) for _ in range(m)] for m in [A, B, Q]]

S = [-INF] + S + [INF]
T = [-INF] + T + [INF]

for x in X:
    s_i = bisect(S, x)
    t_i = bisect(T, x)
    points = [S[s_i-1], S[s_i], T[t_i-1], T[t_i]]
    min_cost = INF
    for j, p_j in enumerate(points):
        for k, p_k in enumerate(points):
            # 神社同士、寺同士は比べない
            if j//2 == k//2:
                continue
            cost = abs(p_j-x) + abs(p_k-p_j)
            min_cost = min(min_cost, cost)
    print(min_cost)
