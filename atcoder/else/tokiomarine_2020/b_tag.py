A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

dist = abs(A-B)
speed_diff = V-W
if speed_diff <= 0:
    print("NO")
    exit()

if -(-dist//speed_diff) <= T:
    print("YES")
else:
    print("NO")
