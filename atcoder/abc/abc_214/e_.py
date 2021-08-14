# 区間が与えられたとき l の時点で r を priority queue に追加するという典型

T = int(input())

ans_list = []
for _ in range(T):
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]

    LR.sort()
    bl, br = -1, -1
    x = -1
    ans = "Yes"
    for l, r in LR:
        if br < l:
            x = l
        else:
            x = max(x+1, l)
        # print((l, r), x)
        if r < x:
            ans = "No"
            break
        bl, br = l, r
    ans_list.append(ans)

print(*ans_list, sep='\n')
