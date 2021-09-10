N = int(input())
VWXYZ = [list(map(int, input().split())) for _ in range(N)]

ans = sum(sum(vwxyz) < 20 for vwxyz in VWXYZ)
print(ans)