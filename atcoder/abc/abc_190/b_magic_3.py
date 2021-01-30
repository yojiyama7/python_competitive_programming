N, S, D = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]

if any(x < S and y > D for x, y in XY):
    print("Yes")
else:
    print("No")