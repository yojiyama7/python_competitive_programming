from collections import deque

N = int(input())
A = [list(map(int, input().split()))[::-1] for _ in range(N)]

# pop_count = 0
l = [[0 for _ in range(N+1)] for _ in range(N+1)]
day = 0
q = deque([(i+1, a.pop()) for i, a in enumerate(A)])

while q:
    day += 1
    r = deque()
    while q:
        p = q.popleft()
        # print(p)
        # if p == "m":
        #     q.append("m")
        #     day += 1
        #     continue
        x, y = p
        if x > y:
            x, y = y, x
        l[x][y] += 1
        if l[x][y] >= 2:
            l[x][y] -= 2
            if A[x-1]:
                r.append((x, A[x-1].pop()))
            if A[y-1]:
                r.append((y, A[y-1].pop()))
    q = r

if all(map(len, A)):
    print(-1)
else:
    print(day)

################################

# from collections import deque
# N = int(input())
# A = [deque([(int(s), i+1) for i, s in enumerate(input().split())]) for _ in range(N)]

# l = [[0 for _ in range(N+1)] for _ in range(N+1)]

# count = 0
# q = deque([(i+1, *a.popleft()) for i, a in enumerate(A)])
# # print(q)
# while q:
#     p = q.popleft()
#     # print(p)
#     x, y, d = p
#     if x > y:
#         x, y = y, x
#     l[x][y] += 1
#     if l[x][y] >= 2:
#         l[x][y] -= 2
#         count = max(count, d)
#         if A[x-1]:
#             q.append((x, *A[x-1].popleft()))
#         if A[y-1]:
#             q.append((y, *A[y-1].popleft()))

# if all(map(len, A)):
#     print(-1)
# else:
#     print(count)
    
