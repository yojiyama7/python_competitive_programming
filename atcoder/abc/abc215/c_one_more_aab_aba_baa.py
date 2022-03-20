from itertools import permutations as permu

S, K = input().split()
K = int(K)

l = [''.join(x) for x in permu(S)]
# l = []
# for x in permu(S):
#     l.append(''.join(x))
l = sorted(set(l))
print(l[K-1])

################################

# S, K = input().split()
# K = int(K)

# def solve(x, l):
#     if x == 0:
#         return {""}
#     ans = set()
#     for i in range(x):
#         for p in solve(x-1, l[:i]+l[i+1:]):
#             ans.add(l[i] + p)
#     return ans

# ans = solve(len(S), S)
# ans = sorted(ans)
# print(ans[K-1])
