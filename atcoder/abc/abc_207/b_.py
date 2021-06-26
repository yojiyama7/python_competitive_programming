A, B, C, D = map(int, input().split())

if D*C-B == 0:
    print(-1)
    exit()

ans = -(-A//(D*C-B))
if ans < 0:
    ans = -1
print(ans)
