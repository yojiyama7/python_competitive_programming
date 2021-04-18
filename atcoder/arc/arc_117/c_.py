N = int(input())
C = input()

# mod 3 における二項係数がよくわかっていない
# まずはなぜ普段の方法が使えないのかを理解する
def combi(n, k):
    if f_fact(n) - f_fact(k) - f_fact(n-k) >= 1:
        return (0)
    return g_fact(n) * g_fact(r) * g_fact(n-r) % 3

ans = 1
for i, c in enumerate(C):
    m = "BWR".find(c)
    ans *= -1**(N-1) * combi(N-1, i)
    ans %= 3

print("BWR"[ans])
################################

# # UNCOMPLETE

# 記号を 数字に する
# ピラミッド型 は 二項係数
# (パスカルの三角形)

# from time import sleep

# def to_mark(s):
#     return s.replace("W", "#").replace("R", "=").replace("B", "-")

# def solve_upblock(a, b):
#     if a == b:
#         return a
#     s = set("WRB")
#     s.remove(a)
#     s.remove(b)
#     return list(s)[0]

# def generate_pyramid(l):
#     p = [l]
#     while len(l) > 1:
#         next_l = [solve_upblock(l[j], l[j+1]) for j in range(len(l)-1)]
#         l = next_l
#         p.append("".join(l))
#     return (p[::-1])

# S = input()
# N = len(S)
# # print()
# [print(" "*(N-i)+to_mark(line)) for i, line in enumerate(generate_pyramid(S))]
# # print()

# # for i, line in enumerate(generate_pyramid(S)[::-1]):
# #     print('\r' + line, end=" "*i)
# #     sleep(1)
