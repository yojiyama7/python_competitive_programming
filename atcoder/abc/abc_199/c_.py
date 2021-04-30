N = int(input())
S = input()
Q = int(input())
TAB = [list(map(int, input().split())) for _ in range(Q)]

l = list(S)
margin = 0
for t, a, b in TAB:
    if t == 1:
        a, b = a-1, b-1
        x, y = (a+margin)%(2*N), (b+margin)%(2*N)
        l[x], l[y] = l[y], l[x]
    elif t == 2:
        margin += N
        margin %= 2*N

ans = "".join(l[margin:] + l[:margin])
print(ans)
