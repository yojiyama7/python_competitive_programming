from bisect import bisect_left

INF = 10**18

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.append(-INF)
B.append(INF)
B.sort()

ans = INF
for a in A:
    idx = bisect_left(B, a)
    ans = min(
        ans,
        abs(a-B[idx]),
        abs(a-B[idx-1])
    )

print(ans)
