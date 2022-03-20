N = int(input())
P = list(map(int, input().split()))

q = [(p, i) for i, p in enumerate(P, start=1)]
q.sort()
ans = [y for _, y in q]
print(*ans)

################################

# N = int(input())
# P = list(map(int, input().split()))

# ans = [-1]*N
# for i, p in enumerate(P):
#     ans[p-1] = i+1

# print(*ans)