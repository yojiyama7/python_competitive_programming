

################################

# 複素平面で表現 できmasenndesita

# N = int(input())
# AB = [complex(*map(int, input().split())) for _ in range(N)]
# CD = [complex(*map(int, input().split())) for _ in range(N)]

# AB_center = sum(AB)
# CD_center = sum(CD)
# AB_moved = [ab - AB_center for ab in AB]
# CD_moved = [cd - CD_center for cd in CD]
# for ab in AB_moved:
#     if ab:
#         break

################################

# # 何がダメなのこの実装

# from math import atan2, degrees, pi

# N = int(input())
# AB = [list(map(int, input().split())) for _ in range(N)]
# CD = [list(map(int, input().split())) for _ in range(N)]

# if N == 1:
#     print("Yes")
#     exit()

# A, B = zip(*AB)
# C, D = zip(*CD)
# ac, bc = (sum(A), sum(B))
# cc, dc = (sum(C), sum(D))

# s_dist_angles = []
# for a, b in AB:
#     a *= N
#     b *= N
#     x, y = (a-ac, b-bc)
#     ans = ((x**2 + y**2), atan2(y, x))
#     s_dist_angles.append(ans)
# t_dist_angles = []
# for c, d in CD:
#     c *= N
#     d *= N
#     x, y = (c-cc, d-dc)
#     ans = ((x**2 + y**2), atan2(y, x))
#     t_dist_angles.append(ans)

# # print(s_angle_dists, t_angle_dists)

# MAX_DIFF = 10**-2
# def almost_equal_rad(a, b):
#     a %= 2*pi
#     b %= 2*pi
#     if abs(a - b) > MAX_DIFF:
#         return False
#     return True

# dist, angle = s_dist_angles[1] if s_dist_angles[0][0] == 0 else s_dist_angles[0]
# p = [(sd, (sa-angle)%(2*pi)) for sd, sa in s_dist_angles]
# for i in range(N):
#     dist, angle = t_dist_angles[i]
#     q = [(td, (ta-angle)%(2*pi)) for td, ta in t_dist_angles]
#     p.sort()
#     q.sort()
#     print(i)
#     print(p)
#     print(q)
#     flag = True
#     print([almost_equal_rad(pa, qa) for (pd, pa), (qd, qa) in zip(p, q)])
#     for (pd, pa), (qd, qa) in zip(p, q):
#         if almost_equal_rad(pa, qa) and pd == qd:
#             continue
#         flag = False
#     if flag:
#         print("Yes")
#         exit()
# print("No")

################################

# from math import atan2, cos, sin

# MAX_DIFF = 1/10**7

# class Vec2:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __mul__(self, other):
#         if isinstance(other, Vec2):
#             return
#         return Vec2(self.x*other, self.y*other)
#     def __add__(self, other):
#         if isinstance(other, Vec2):
#             return Vec2(self.x+other.x, self.y+other.y)
#     def __sub__(self, other):
#         if isinstance(other, Vec2):
#             return Vec2(self.x-other.x, self.y-other.y)
#     def __lt__(self, other):
#         if isinstance(other, Vec2):
#             return tuple(self) < tuple(other)
#     def __iter__(self):
#         return iter([self.x, self.y])
#     def __repr__(self):
#         return "V"+str((self.x, self.y))

#     def rotate_origin(self, rotate_rad):
#         tilt_rad = atan2(self.y, self.x)
#         tilt_rad += rotate_rad
#         r = (self.x**2 + self.y**2) ** (1/2)
#         ans = Vec2(r*cos(tilt_rad), r*sin(tilt_rad))
#         return ans

#     def almost_equal(self, other):
#         if isinstance(other, Vec2):
#             if abs(self.x - other.x) > MAX_DIFF:
#                 return False
#             if abs(self.y - other.y) > MAX_DIFF:
#                 return False
#             return True

#     def atan2(self):
#         return atan2(self.y, self.x)

# class Vec2Set:
#     def __init__(self, vecs):
#         self.vecs = list(vecs)

#     def __add__(self, other):
#         return Vec2Set([vec + other for vec in self.vecs])
#     def __sub__(self, other):
#         return Vec2Set([vec - other for vec in self.vecs])
#     def __mul__(self, other):
#         return Vec2Set([vec * other for vec in self.vecs])
#     def __iter__(self):
#         return iter(self.vecs)

#     # O(N log N)
#     def compare_almost_equal(self, other):
#         if isinstance(other, Vec2Set):
#             # print(self.vecs)
#             # print(other.vecs)
#             a = sorted(self.vecs)
#             b = sorted(other.vecs)
#             # print(sorted_zip)
#             for ai, bi in zip(a, b):
#                 if not ai.almost_equal(bi):
#                     return False
#             return True

#     def rotate_origin(self, rotate_rad):
#         ans = Vec2Set([vec.rotate_origin(rotate_rad) for vec in self.vecs])
#         return ans

# N = int(input())
# AB = [list(map(int, input().split())) for _ in range(N)]
# CD = [list(map(int, input().split())) for _ in range(N)]

# S = Vec2Set(Vec2(a, b) for a, b in AB)
# T = Vec2Set(Vec2(c, d) for c, d in CD)

# S_xN = S * N
# T_xN = T * N

# S_xN_center = sum(S.vecs, Vec2(0, 0))
# T_xN_center = sum(T.vecs, Vec2(0, 0))

# # print(S_xN_center, T_xN_center)

# P = S_xN_moved = S_xN - S_xN_center
# Q = T_xN_moved = T_xN - T_xN_center

# P_rotated = P.rotate_origin(-P.vecs[0].atan2())
# print([f"({v.x:.5}, {v.y:.5})" for v in P_rotated.vecs])
# # print(P_rotated.vecs[0], P_rotated.vecs[0].atan2())
# Q.vecs = sorted(Q.vecs, key=lambda x:x.atan2())
# for i in range(N):
#     Q_rotated = Q.rotate_origin(-Q.vecs[i].atan2())
#     # pivot = P.vecs
#     # if Q_rotated.vecs[i].almost_equal(pivot):
#     #     print(i, )
#     #     print([f"({v.x:.5}, {v.y:.5})" for v in Q_rotated.vecs[i:]+Q_rotated.vecs[:i]])
#     # print(i, Q.vecs[i].atan2())
#     if P_rotated.compare_almost_equal(Q_rotated):
#         print("Yes")
#         exit()
# print("No")

################################

# from math import atan2

# N = int(input())
# AB = [list(map(int, input().split())) for _ in range(N)]
# CD = [list(map(int, input().split())) for _ in range(N)]

# A, B = zip(*AB)
# C, D = zip(*CD)

# s_xy = [(a*N, b*N) for a, b in AB]
# t_xy = [(c*N, d*N) for c, d in CD]

# # 座標を N 倍した時の S と T の重心
# scx, scy = sum(A), sum(B)
# tcx, tcy = sum(C), sum(D)

# # (distance, angle) 重心からの距離と angle
# s_da = []
# for x, y in s_xy:
#     x -= scx
#     y -= scy
#     d = x**2 + y**2
#     a = atan2(y, x)
#     s_da.append((d, a))
# t_da = []
# for x, y in t_xy:
#     x -= tcx
#     y -= tcy
#     d = x**2 + y**2
#     a = atan2(y, x)
#     t_da.append((d, a))

# s_da.sort()
# t_da.sort()

# for s_da_i, t_da_i in zip(s_da, t_da):

################################

# # N頂点集合のi番目が Xi, Yi だとする
# # 図形の重心は (SUM(X1~XN)/N, SUM(Y1~YN)/N) である
# # 2つの図形の重心を求めて重ね、回転によって一致するか考える

# # 図形の重心がキモっぽい　知らんわｋす

# from math import radians, atan2, cos, sin

# N = int(input())
# AB = [list(map(int, input().split())) for _ in range(N)]
# CD = [list(map(int, input().split())) for _ in range(N)]

# def rotate(p, deg):
#     x, y = p
#     d = atan2(y, x) + radians(deg)
#     r = (x**2 + y**2) ** (1/2)
#     a, b = cos(d)*r, sin(d)*r
#     return (a, b)

# sx, sy = AB[0]
# p = [(a-sx, b-sy) for a, b in AB]
# for i in range(3600):
#     deg = i/10
#     # print(deg)
#     for sc, sd in CD:
#         q = []
#         for c, d in CD:
#             q.append((c-sc, d-sd))
#         q = list(map(lambda x: rotate(x, deg), q))
#         if deg == 90:
#             print(p, q)
#         if all(abs(x-a) <= 10**-4 and abs(b-y) <= 10**-4 for (x, y), (a, b) in zip(p, q)):
#             print("Yes")
#             exit()

# print("No")

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
