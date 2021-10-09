# dp 配列省略は結構高速化になる
# 本番中に書いたコードがなぜREなのかきになる
# --- pypy特有の問題か俺のコードがpython的にoutか
# --- python でも RE したからコードが問題そう
# --- 単に添え字ミスでした　添え字に使うような値は変数に入れろカス、です。
# 何もわからん時は思いついたことをする。それしないでAC逃してるし。

from collections import deque

INF = 10**18
MOD = 998244353

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
UV = [list(map(int, input().split())) for _ in range(N-1)]
# N, M, K = 1000, 100, 9891
# A = [1, N] * (N//2)
# UV = [(i, i+1) for i in range(1, N)]

g = [set() for _ in range(N)]
for i, (u, v) in enumerate(UV):
    u -= 1
    v -= 1
    g[u].add((v, i))
    g[v].add((u, i))

cnt = [0]*(N-1)
for i in range(M-1):
    s, e = A[i]-1, A[i+1]-1
    dist = [INF]*N
    dist[s] = 0
    q = deque([s])
    while q:
        t = q.popleft()

        for to, _ in g[t]:
            if dist[to] <= dist[t] + 1:
                continue
            dist[to] = dist[t] + 1
            q.append(to)
    p = e
    while p != s:
        for to, edge_idx in g[p]:
            if dist[to] == dist[p] - 1:
                p = to
                cnt[edge_idx] += 1
                break
        # print(g[p], (s, e), p, dist)

cnt_sum = sum(cnt)
# print("cnt", cnt, cnt_sum)
if (cnt_sum-K) % 2 == 1:
    print(0)
    exit()

b = (cnt_sum-K)//2
# print(f"b: {b}")
if not (0 <= b <= cnt_sum):
    # print('xz')
    print(0)
    exit()

b = min(b, cnt_sum-b)

prices = []
zero = 0
for cnt_i in cnt:
    if cnt_i:
        prices.append(cnt_i)
    else:
        zero += 1

# print(prices)

dp = [0 for j in range(b+1)] 
dp[0] = 1
for i in range(1, len(prices)+1):
    p = prices[i-1]
    dp_new = [0 for j in range(b+1)] 
    for j in range(b+1):
        dp_new[j] = dp[j]
        if j-p >= 0:
            dp_new[j] += dp[j-p]
            dp_new[j] %= MOD
    dp = dp_new
    # if i%10 == 0:
    #     print(i)

# [print(dp_i) for dp_i in dp]

ans = dp[b]
ans *= pow(2, zero, MOD)
ans %= MOD
print(ans)

################################

# from collections import deque

# INF = 10**18
# MOD = 998244353

# N, M, K = map(int, input().split())
# A = list(map(int, input().split()))
# UV = [list(map(int, input().split())) for _ in range(N-1)]
# # N, M, K = 1000, 100, 9891
# # A = [1, N] * (N//2)
# # UV = [(i, i+1) for i in range(1, N)]

# g = [set() for _ in range(N)]
# for i, (u, v) in enumerate(UV):
#     u -= 1
#     v -= 1
#     g[u].add((v, i))
#     g[v].add((u, i))

# cnt = [0]*(N-1)
# for i in range(M-1):
#     s, e = A[i]-1, A[i+1]-1
#     dist = [INF]*N
#     dist[s] = 0
#     q = deque([s])
#     while q:
#         t = q.popleft()

#         for to, _ in g[t]:
#             if dist[to] <= dist[t] + 1:
#                 continue
#             dist[to] = dist[t] + 1
#             q.append(to)
#     p = e
#     while p != s:
#         for to, edge_idx in g[p]:
#             if dist[to] == dist[p] - 1:
#                 p = to
#                 cnt[edge_idx] += 1
#                 break
#         # print(g[p], (s, e), p, dist)

# cnt_sum = sum(cnt)
# # print("cnt", cnt, cnt_sum)
# if (cnt_sum-K) % 2 == 1:
#     print(0)
#     exit()

# b = (cnt_sum-K)//2
# # print(f"b: {b}")
# if not (0 <= b <= cnt_sum):
#     # print('xz')
#     print(0)
#     exit()

# b = min(b, cnt_sum-b)

# prices = []
# zero = 0
# for cnt_i in cnt:
#     if cnt_i:
#         prices.append(cnt_i)
#     else:
#         zero += 1

# # print(prices)

# dp = [[0 for j in range(b+1)] for i in range(len(prices)+1)]
# dp[0][0] = 1
# for i in range(1, len(prices)+1):
#     p = prices[i-1]
#     for j in range(b+1):
#         dp[i][j] = dp[i-1][j]
#         if j-p >= 0:
#             dp[i][j] += dp[i-1][j-p]
#             dp[i][j] %= MOD
#     # if i%10 == 0:
#     #     print(i)

# # [print(dp_i) for dp_i in dp]

# ans = dp[len(prices)][b]
# ans *= pow(2, zero, MOD)
# ans %= MOD
# print(ans)
