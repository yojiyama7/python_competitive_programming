# AC

from heapq import *

# ここは有限じゃないとダメ ネーミングはINFでいいのか問題
INF = 10**20

class HeapMin:
    def __init__(self, l=[], key=lambda x:x):
        self.key = key
        self.l = [(self.key(l_i), l_i) for l_i in l]
        heapify(self.l)

    # def top(self):
    #     return self.l[0][1]

    def push(self, v):
        heappush(self.l, (self.key(v), v))

    def pop(self):
        _, r = heappop(self.l)
        return r

    def __bool__(self):
        return len(self.l) > 0

N, K = map(int, input().split())
TD = [list(map(int, input().split())) for _ in range(N)]

# 番兵式
l = [[-INF] for _ in range(N)]
for t, d in TD:
    t, d = t-1, d
    l[t].append(d)

[l_i.sort(reverse=True) for l_i in l]
l.sort(reverse=True)

# score: 各種類の最大値の上からK個の総和
# q: score に足されていない寿司たち(あまり)
score = 0
q = HeapMin([], key=lambda x: -x)
for i in range(K):
    score += l[i][0]
    for r in l[i][1:]:
        q.push(r)
for i in range(K, N):
    for r in l[i]:
        q.push(r)

max_score = score + K**2
for x in reversed(range(1, K)):
    v = l[x][0]
    w = q.pop()
    q.push(w)
    if v < w:
        q.pop()
        score += w
        q.push(v)
        score -= v
    max_score = max(score + x**2, max_score)

print(max_score)

################################

# # この方針(番兵なし)でクリアできないのかしら

# # あんまり凝った実装にしない方が良い
# # シンプル(直感的)に実装した方が良さげ

# from heapq import *

# N, K = map(int, input().split())
# TD = [list(map(int, input().split())) for _ in range(N)]

# class HeapMin:
#     def __init__(self, l=[], key=lambda x:x):
#         self.key = key
#         self.l = [(self.key(l_i), l_i) for l_i in l]
#         heapify(self.l)

#     def top(self):
#         return self.l[0][1]

#     def push(self, v):
#         heappush(self.l, (self.key(v), v))

#     def pop(self):
#         _, r = heappop(self.l)
#         return r

#     def __bool__(self):
#         return len(self.l) > 0

# score = 0
# q = HeapMin([], key=lambda x: -x)
# max_point = [0]*N
# for t, d in TD:
#     t, d = t-1, d
#     if max_point[t] < d:
#         q.push(max_point[t])
#         max_point[t] = d
#     else:
#         q.push(d)

# max_point.sort(reverse=True)
# while max_point[-1] == 0:
#     max_point.pop()
# # print(max_point, q.l)
# max_type = min(K, len(max_point))
# score = sum(max_point[:max_type])
# # print((K, score))
# max_num = score + max_type**2
# for x in reversed(range(1, max_type)):
#     if max_point[x] < q.top():
#         score += q.pop()
#         score -= max_point[x]
#         q.push(max_point[x])
#         # print((x, score))
#     print((x, score))
#     max_num = max(max_num, score + x**2)

# print(max_num)

################################

# # 方針ミス

# from itertools import accumulate as acc
# from bisect import bisect_left, bisect_right

# N, K = map(int, input().split())
# TD = [list(map(int, input().split())) for _ in range(N)]

# m = [0]*N
# p = []
# for t, d in TD:
#     t, d = t-1, d
#     m[t] = max(m[t], d)
#     p.append(d)

# # 降順でソートして累積和する方針で行く
# m.sort(reverse=True)
# p.sort(reverse=True)
# m_acc = [0] + list(acc(m))
# p_acc = [0] + list(acc(p))

# # 降順でy個目までの寿司を選んだ時のまだ選ばれていない寿司の数 + x <= K
# def is_ok(x, y):
#     cnt = N - bisect_left(m[::-1], p[y-1])
#     remain = y - cnt
#     return remain + x <= K

# # x種類以上選ぶ時の、美味しさの総和の最大値
# def f(x):
#     score1 = m_acc[x]

#     ok, ng = 0, N+1
#     while abs(ok - ng) > 1:
#         mid = (ok+ng)//2
#         if is_ok(x, mid):
#             ok = mid
#         else:
#             ng = mid
#     cnt = N - bisect_left(m[::-1], p[ok-1])
#     score2 = p_acc[ok] - m_acc[cnt]
#     score = score1 + score2
#     return score

# ans = 0
# for x in range(N+1):
#     if x > K:
#         continue
#     # print(x, f(x), f(x)+x**2)
#     ans = max(ans, f(x) + x**2)
# print(ans)

################################

# # 詰め甘くて頭バグった

# from itertools import accumulate as acc
# from bisect import bisect_left, bisect_right

# N, K = map(int, input().split())
# TD = [list(map(int, input().split())) for _ in range(N)]

# max_points = [0]*N
# points = []
# for t, d in TD:
#     t, d = t-1, d
#     max_points[t] = max(max_points[t], d)
#     points.append(d)

# max_points.sort()
# points.sort()

# max_points_acc = [0] + list(acc(max_points))
# points_acc = [0] + list(acc(points))

# def sum_range_acc(a, l, r):
#     return a[r] - a[l]

# def is_ok(x, y, remain):
#     all_cnt = y
#     max_cnt = bisect_right(max_points[-x:], points[y-1])
#     cnt = all_cnt - max_cnt
#     return cnt <= remain

# ans = 0
# for x in range(N+1):
#     if K < x:
#         continue
#     score1 = sum_range_acc(max_points_acc, N-x, N)
#     ok, ng = 0, N+1
#     print(x, K-x)
#     while abs(ok - ng) > 1:
#         mid = (ok + ng) // 2
#         if is_ok(x, mid, K-x):
#             ok = mid
#         else:
#             ng = mid
#     max_cnt = bisect_right(max_points[-x:], points[ok-1])
#     print(ok, max_cnt)
#     score2 = sum_range_acc(points_acc, N-ok, N) - sum_range_acc(max_points_acc, N-max_cnt, N)
#     print(score1, score2, x**2)
#     score = score1 + score2 + x**2
#     ans = max(ans, score)
# print(ans)

################################

# # ヒープ以降をどう実装するかわからんな
# # キレそう。heap in heap とか？ 考えてからコード書いた方が良さげ

# def swap(array, i, j):
#     array[i], array[j] = array[j], array[i]

# class Heap:
#     def __init__(self, nums=[]):
#         self.is_used = False
#         self.size = 0
#         self.nums = []
#         for num in nums:
#             self.insert(num)

#     def insert(self, num):
#         self.nums.append(num)
#         self.size += 1

#         i = self.size-1
#         while not (i == 0 or self.nums[i] < self.nums[(i-1)//2]):
#             swap(self.nums, i, (i-1)//2)
#             i = (i-1)//2

#     def __repr__(self):
#         return f'<{" ".join(map(str, self.nums))}>'

#     def get_root(self):
#         return self.nums[0]

#     def pop_root(self):
#         print(f"size: {self.size}")
#         if self.size == 0:
#             return False
#         root = self.nums[0]
#         v = self.nums.pop()
#         self.size -= 1
#         if self.size == 0:
#             return root

#         i = 0
#         while i*2+1 < self.size:
#             c1, c2 = i*2+1, i*2+2
#             if c2 < self.size and self.nums[c2] > self.nums[c1]:
#                 c1 = c2
#             if self.nums[c1] <= v:
#                 break
#             self.nums[i] = self.nums[c1]
#             i = c1
#         self.nums[i] = v
#         return root

#     def __lt__(self, other):
#         return self.get_root() < other.get_root()
#     def __le__(self, other):
#         return self.get_root() <= other.get_root()
#     def __eq__(self, other):
#         return self.get_root() == other.get_root()
#     def __ne__(self, other):
#         return self.get_root() != other.get_root()
#     def __gt__(self, other):
#         return self.get_root() > other.get_root()
#     def __ge__(self, other):
#         return self.get_root() >= other.get_root()


# # l = list(range(32, -1, -1))[::-1]
# # h = Heap(l)
# # # print(h)
# # # print(h.pop_root())
# # # print(h)
# # for i in range(h.size):
# #     print(h.pop_root())

# N, K = map(int, input().split())
# TD = [list(map(int, input().split())) for _ in range(N)]

# e = [Heap() for _ in range(N+1)]
# for t, d in TD:
#     e[t].insert(d)
# hq = Heap(e)

# added_hq = Heap()
# score = 0
# for i in range(K):
#     r = hq.pop_root()
#     score += r.pop_root()