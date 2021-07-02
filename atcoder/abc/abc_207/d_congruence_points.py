# N頂点集合のi番目が Xi, Yi だとする
# 図形の重心は (SUM(X1~XN)/N, SUM(Y1~YN)/N) である
# 2つの図形の重心を求めて重ね、回転によって一致するか考える

# 図形の重心がキモっぽい　知らんわｋす

from math import radians, atan2, cos, sin

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(N)]

def rotate(p, deg):
    x, y = p
    d = atan2(y, x) + radians(deg)
    r = (x**2 + y**2) ** (1/2)
    a, b = cos(d)*r, sin(d)*r
    return (a, b)

sx, sy = AB[0]
p = [(a-sx, b-sy) for a, b in AB]
for i in range(3600):
    deg = i/10
    # print(deg)
    for sc, sd in CD:
        q = []
        for c, d in CD:
            q.append((c-sc, d-sd))
        q = list(map(lambda x: rotate(x, deg), q))
        if deg == 90:
            print(p, q)
        if all(abs(x-a) <= 10**-4 and abs(b-y) <= 10**-4 for (x, y), (a, b) in zip(p, q)):
            print("Yes")
            exit()

print("No")

################################

# # これがマジでカス
# # 初動もひどかったので激冷えです

# INF = float('inf')

# N = int(input())
# AB = [list(map(int, input().split())) for _ in range(N)]
# CD = [list(map(int, input().split())) for _ in range(N)]

# def is_on_line(l):
#     s_set = set()
#     for i in range(len(l)-1):
#         x, y = l[i]
#         a, b = l[i+1]
#         s = (y-b) / (x-a) if (x-a) != 0 else INF
#         s_set.add(s)
#     if len(s_set) == 1:
#         return True
#     else:
#         return False

# # 1直線に並んでいる場合
# if is_on_line(AB) and is_on_line(CD):
#     AB.sort()
#     d1 = []
#     for i in range(N-1):
#         x, y = AB[i]
#         a, b = AB[i+1]
#         d = (a-x)**2 + (b-y)**2
#         d1.append(d)
#     CD.sort()
#     d2 = []
#     for i in range(N-1):
#         x, y = CD[i]
#         a, b = CD[i+1]
#         d = (a-x)**2 + (b-y)**2
#         d2.append(d)
#     if d1 == d2 or d1 == d2[::-1]:
#         print("Yes")
#     else:
#         print("No")
#     exit()

# def rotate90(p):
#     x, y = p
#     return (y, -x)

# # 回転は 90度単位しかありえない? <- そんなことない <- 2点の時のみ? <- 1直線に並んでいる場合かな
# # 回転(4通り) Sの基準点(N通り) Tの基準点(N通り)

# for i in range(4):
#     for j in range(N):
#         abx, aby = AB[j]
#         for k in range(N):
#             cdx, cdy = CD[k]
#             p = [(a-abx, b-aby) for a, b in AB]
#             q = [(c-cdx, d-cdy) for c, d in CD]
#             p.sort()
#             q.sort()
#             if p == q:
#                 print("Yes")
#                 exit()
#     CD = list(map(rotate90, CD))

# print("No")

# # def angle(p1, p2):
# #     x, y = p1
# #     a, b = p2
# #     return atan2(b-y, a-x)

# # def rotate(p, deg):
# #     x, y = p
# #     d = atan2(y, x) + deg
# #     r = (x**2 + y**2) ** (1/2)
# #     a, b = cos(d)*r, sin(d)*r
# #     return (a, b)

# # for i, (sa, sb) in enumerate(AB):
# #     for j, (sc, sd) in enumerate(CD):
# #         p = [(a-sa, b-sb) for a, b in AB]
# #         p.sort()
# #         q = [(c-sc, d-sd) for c, d in CD]
# #         print(p)
# #         for k in range(N):
# #             if j == k:
# #                 continue
# #             d = angle((sc, sd), q[k])
# #             l = [rotate(qi, d) for qi in q]
# #             l.sort()
# #             if p == l:
# #                 print("Yes")
# #                 exit()

# # print("No")
