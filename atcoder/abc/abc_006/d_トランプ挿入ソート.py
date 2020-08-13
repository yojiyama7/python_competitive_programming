from bisect import bisect_left

N = int(input())
C = [int(input()) for _ in range(N)]

l = [C[0]]
for c in C[1:]:
    if c > l[-1]:
        l.append(c)
    else:
        l[bisect_left(l, c)] = c
print(N-len(l))
