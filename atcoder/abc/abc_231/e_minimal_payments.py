N, X = map(int, input().split())
A = list(map(int, input().split()))

# 0-idx: A[i:] で p 円支払う
memo = dict()
def solve(i, p):
    if i == N-1:
        return p//A[i]
    if (i, p) in memo:
        return memo[(i, p)]
    floor_p = p//A[i+1]*A[i+1]
    ceil_p = -(-p//A[i+1])*A[i+1]
    ans = min(
        solve(i+1, floor_p) + (p-floor_p)//A[i],
        solve(i+1, ceil_p) + (ceil_p-p)//A[i]
    )
    memo[(i, p)] = ans
    return ans

ans = solve(0, X)
print(ans)

################################

# N, X = map(int, input().split())
# A = list(map(int, input().split()))

# # X円を支払う
# ## -> [ceil(X/a)] 円払って [お釣り]を受け取る
# ## -> [floor(x/a)] + A[i-1]*K枚 を払って お釣りをなくす
# ## A[i] の倍数 についてだけ考えれるようにしておく -> それについてしか解決できない
# ## (1, 10, 100) の場合、 10以上で支払えるのは倍数だけであり そうでない数については 1 であらかじめ調整しておく必要がある
# ## 硬貨1の調整は, ぴったし支払う or 10を支払いお釣りをもらう であり
# ## 87 を例にすると 7円支払う=7枚 or 硬貨10+お釣り3枚=4枚 の どちらかが最適である
# ## 7未満では金額が不足するし、8,9枚支払っても支払い,お釣ともにコインの枚数が増えるだけである
# ## すなわち (1, 10, 100) で87円支払うコスト というのは
# ## (10, 100) で80円支払うコスト+7 または
# ## (10, 100) で90円支払うコスト+3
# ## のどちらかである
# ##

# A.sort()
# # 各硬貨について 切り上げるか 切り下げるか を考える

# memo = dict()
# def solve(x, i):
#     if (x, i) in memo:
#         return memo[(x, i)]
#     if i == 0:
#         return x

#     a = A[i]
#     ceiling = -(-X//a)*a
