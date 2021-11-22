from bisect import bisect_right

N, K = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]

l = [sum(p) for p in P]
q = sorted(l)

for li in l:
    cnt = N - bisect_right(q, li+300)
    rank = cnt + 1
    if rank <= K:
        print("Yes")
    else:
        print("No")
