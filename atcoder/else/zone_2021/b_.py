N, D, H = map(int, input().split())
DH = [list(map(int, input().split())) for _ in range(N)]

max_num = 0
for d, h in DH:
    a = D - d
    b = H - h
    x = H - b*D/a
    max_num = max(x, max_num)

print(max_num)