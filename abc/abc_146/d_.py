# 簡単な全探索なはずだが、、、
# 構想が浮かばん

# N = int(input())
# AB = [list(map(int, input().split())) for _ in range(N-1)]

# colors = [0]*(N-1)

# d = [[] for _ in range(N)]
# for i, (a, b) in enumerate(AB):
#     d[a-1].append((b-1, i))
#     d[b-1].append((a-1, i))

# visited = [0]*N
# q = [0]
# while q:
#     t = q.pop()

#     used = 0
#     for x, index in d[t]:
#         if visited[x]:
#             used = colors[x]
#     color = 1
#     for x, index in d[t]:
#         if color == used:
#             color += 1
#         colors[index] = color
#         color += 1

# print(max(colors))
# for c in colors:
#     print(c)
    
