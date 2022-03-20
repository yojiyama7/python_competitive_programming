N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

S_set = set(S)
T_set = set(T)

if T_set - S_set:
    print(-1)
    exit()

cost = 0
idx = 0
while idx < M and S[0] == T[idx]:
    cost += 1
    idx += 1

if idx < M:
    r = S.index(T[idx])
    l = S[::-1].index(T[idx]) + 1
    cost += min(l, r)
    cost += 1
    idx += 1

while idx < M:
    cost += (T[idx-1] != T[idx])
    cost += 1
    idx += 1

print(cost)

# cost = 0
# is_betweened = False
# bt = None
# for i, t in enumerate(T):
#     if is_betweened:
#         cost += bt != t
#         cost += 1
#         continue
#     if S[0] != t:
#         r = S.index(t)
#         l = S[::-1].index(t)+1
#         cost += min(l, r)
#         is_betweened = True
#     cost += 1
#     bt = t

# print(cost)
