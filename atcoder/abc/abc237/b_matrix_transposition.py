H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

l = list(zip(*A))
[print(*li) for li in l]