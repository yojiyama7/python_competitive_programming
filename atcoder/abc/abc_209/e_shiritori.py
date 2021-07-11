import sys
sys.setrecursionlimit(10**8)

N = int(input())
S = [input() for _ in range(N)]

def to_num_inner(c):
    if ord('a') <= ord(c) <= ord('z'):
        return ord(c) - ord('a')
    else:
        return ord(c) - ord('A') + 26

def to_num(t):
    x = 0
    for i, t_i in enumerate(t):
        x += 52**i * to_num_inner(t_i)
    return x

g = [set() for _ in range(52**3)]
for s in S:
    f, e = to_num(s[:3]), to_num(f[-3:])
    g[f].add(e)

result = [-1]*(52**3)
# def solve(i):
#     g[]