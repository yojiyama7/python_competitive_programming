

################################

# 最小全域木 クラスカル法を高速化する気持ち
# ある操作によって 辺が何本追加されるか(A) を検討していたが
# ある操作時点で 連結成分が何個になるか(B) を検討することで解ける問題だった
# A は B に対して "差" となる
# A を求めたい時に それが差として現れる B を考えることで解けるとも言える

# N, M = map(int, input().split())
# AC = [list(map(int, input().split())) for _ in range(M)]

# AC.sort(key=lambda ac: ac[1])

# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a%b)

# yakusu = [0]*int(N**(1/2)+2)
# baisu = 0
# cost = 0
# p = N
# for a, c in AC:
#     # # 約数が既にあるなら
#     # if cost:
#     #     continue
#     # # 倍数が既に
#     # if cost:
#     #     # あるなら
#     #     x = "baisu"
#     #     cnt = a//x-1
#     #     cost += c * cnt
#     # else:
#     #     # ないなら
#     #     cost += 1
#     if a < int(N**(1/2)+2) and yakusu[a] == 0:
#         for b in range(a+a, int(N**(1/2)+2), a):
#             yakusu[b] = 1
