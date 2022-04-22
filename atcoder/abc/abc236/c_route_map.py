N, M = map(int, input().split())
S = input().split()
T = set(input().split())

for s in S:
    res = "Yes" if s in T else "No"
    print(res)