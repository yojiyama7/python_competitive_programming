from itertools import permutations as permu

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

l = [list(s) for s in permu(range(1, N+1))]
l.sort()

print(abs(l.index(P)-l.index(Q)))