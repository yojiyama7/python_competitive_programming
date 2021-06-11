# N = int(input())
# ABCDE = [list(map(int, input().split())) for _ in range(N)]



# for abcde1 in ABCDE:
#     for abcde2 in ABCDE:
#         abcde = map(max, zip(abcde1, abcde2))
#         abcde_min = min(abcde)


################################

# dp遷移が分かりませんでした
# bit dp 的なものだと思ったんだけどな
# bit dp 遷移の, 全ての sub_set に対しての any を取るのがむずい
# なああああああああああにがdpじゃ
# にぶたんの is_ok を別の問題として書き直して整理しなおすべきだった
# 同じ人選ぶことで得がないという自明にも気づくべきだった
# これはこころにくるううううう

N = int(input())
ABCDE = [list(map(int, input().split())) for _ in range(N)]

# ABCDE = [None] + ABCDE

def to_bit(abcde, x):
    ans = 0
    for i, m in enumerate(abcde):
        if m >= x:
            ans |= 1<<i
    return ans

# 普通にfor文？ コンテスト 2分後に解けたわ まじさいごまでやりきったほうがいいわ
def is_ok(x):
    l = [0]*(1<<5)
    l[0] = 1
    for i in range(3):
        p = [0]*(1<<5)
        for j, l_j in enumerate(l):
            for abcde in ABCDE:
                p[j|to_bit(abcde, x)] |= l_j
        l = p
    return l[(1<<5)-1]

    # dp = [[[0 for _ in range(1<<5)] for j in range(4)] for i in range(N+1)]
    # dp[0][0][0] = 1
    # for i in range(N):
    #     abcde = to_bit(ABCDE[i], x)
    #     for j in range(0, 4):
    #         for m in range(1<<5):
    #             dp[i+1][j][m] |= dp[i][j][m]
    #             if j-1 >= 0:
    #                 dp[i+1][j][m|abcde] |= dp[i][j-1][m]
    # print(x, dp)
    # return (dp[N-1][3][(1<<5)-1])

ok, ng = 0, 10**9+1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)