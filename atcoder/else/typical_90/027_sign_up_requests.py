N = int(input())
S = [input() for _ in range(N)]

added = set()
ans = []
for i, s in enumerate(S):
    if s not in added:
        ans.append(i+1)
    added.add(s)

print(*ans, sep='\n')
