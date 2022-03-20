T = int(input())

for _ in range(T):
    N2, N3, N4 = map(int, input().split())

    a, b, c = N2, N4, N3//2

    # 2, 3
    ans = 0
    x = min(b, c)
    b -= x
    c -= x
    ans += x
    # 1, 1, 3
    x = min(a//2, c)
    a -= x*2
    c -= x
    ans += x
    # 1, 2, 2
    x = min(a, b//2)
    a -= x
    b -= x*2
    ans += x
    # 1, 1, 1, 2
    x = min(a//3, b)
    a -= x*3
    b -= x
    ans += x
    # 1, 1, 1, 1, 1
    x = a//5
    a -= x*5
    ans += x

    print(ans)
