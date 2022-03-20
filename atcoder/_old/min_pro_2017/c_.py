# 最小のウンタラカンタラがむずそう

# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# S = [input() for _ in range(N)]

# t = S[A[0]-1]
# for a in A[1:]:
#     u = ""
#     for c1, c2 in zip(t, S[a-1]):
#         if c1 == c2:
#             t += c1
#         else:
#             break
#     t = u
#     S[a-1] = None

# for s in S:
#     if s == None:
#         continue
#     if t == s[:len(t)]:
#         print(-1)
#         exit()
print(t)