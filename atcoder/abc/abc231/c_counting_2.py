from bisect import bisect_left

N, Q = map(int, input().split())
A = list(map(int, input().split()))
X = [int(input()) for _ in range(Q)]

A.sort()
for x in X:
    not_cnt = bisect_left(A, x)
    ans = N - not_cnt
    print(ans)
