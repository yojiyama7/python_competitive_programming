from bisect import bisect_right

N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
l = [-1]*K
for a in A:
    # print(f"a: {a}")
    idx = bisect_right(l, a-1)-1
    # print(f"idx: {idx}")
    if idx < K and a-1 == l[idx]:
        l[idx] = a
    # print(f"l: {l}")

print(sum(l)+K)
