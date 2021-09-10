N = int(input())
P = list(map(int, input().split()))

l = [0]*(200010)
ans = 0
for p in P:
    l[p] = 1
    while l[ans]:
        ans += 1
    print(ans)
