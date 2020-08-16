# 無限ループには入る前aこ
# 無限ループ内のb個

N, K = map(int, input().split())
A = list(map(int, input().split()))

a = [Ai-1 for Ai in A]


visited = [0]*N
visited[0] = 1
p = 0
l = [0]
loop_start = None
while True:
    p = a[p]
    if visited[p]:
        loop_start = l.index(p)
        break
    visited[p] = 1
    # print(p, visited)
    l.append(p)

# print(l, loop_start, K)

if K < loop_start:
    print(l[K])
else:
    print(l[loop_start + (K-loop_start)%(len(l)-loop_start)]+1)
