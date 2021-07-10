# すぐにループしない形の時、ループに入らず終わるパターンを考慮する

N, K = map(int, input().split())
A = list(map(int, input().split()))

A = [-1] + A

loop_pos = None
loop_start_time = None
loop_end_time = None
visited = [-1]*(N+1)
pos = 1
i = 0
while visited[pos] == -1:
    visited[pos] = i
    pos = A[pos]
    i += 1  
    if visited[pos] != -1:
        loop_pos = pos
        loop_start_time = visited[pos]
        loop_end_time = i

# print(loop_start_time, loop_end_time)
w = loop_end_time - loop_start_time
K = min(K, loop_start_time) + max(0, K-loop_start_time)%w
# print(f"K: {K}")

pos = 1
for i in range(K):
    # print(pos)
    pos = A[pos]
print(pos)

################################

# # NOT AC

# # 無限ループには入る前aこ
# # 無限ループ内のb個

# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# a = [Ai-1 for Ai in A]


# visited = [0]*N
# visited[0] = 1
# p = 0
# l = [0]
# loop_start = None
# while True:
#     p = a[p]
#     if visited[p]:
#         loop_start = l.index(p)
#         break
#     visited[p] = 1
#     # print(p, visited)
#     l.append(p)

# # print(l, loop_start, K)

# if K < loop_start:
#     print(l[K])
# else:
#         print(l[loop_start + (K-loop_start)%(len(l)-loop_start)]+1)
