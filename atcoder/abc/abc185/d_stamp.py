N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

l = [0] + A + [N+1]
whites = [l[i+1] - l[i] - 1 for i in range(M+1) if l[i+1] - l[i] - 1]
cnt = 0
if whites:
    stamp_w = min(whites)
    cnt = sum(-(-white // stamp_w) for white in whites)

# print(whites)
print(cnt)