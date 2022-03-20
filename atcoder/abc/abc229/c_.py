# for 文に無駄あり
N, W = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort()

ans = 0
remain = W
for a, b in AB[::-1]:
    if b <= remain:
        gram = b
    else:
        gram = remain
    # print([a, gram])
    ans += a*gram
    remain -= gram

print(ans)