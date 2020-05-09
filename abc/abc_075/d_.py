# N**5 ってま？ だめでした。
# N**4 まで落とせば(2次元累積和)
# いやできんわ
N, K = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]

XY.sort()
x_list, y_list = [list(l) for l in zip(*XY)]

min_area = 10**24
for x1 in x_list:
    for y1 in y_list:
        for x2 in x_list:
            for y2 in y_list:
                if x1 > x2 or y1 > y2:
                    continue
                c = 0
                for x3, y3 in XY:
                    if x1 <= x3 <= x2 and y1 <= y3 <= y2:
                        c += 1
                if c >= K:
                    min_area = min(
                        min_area,
                        (x2-x1)*(y2-y1)
                    )

print(min_area)

################################

# # ダメそうなことはわかる
# N, K = map(int, input().split())
# XY = [list(map(int, input().split())) for _ in range(N)]

# XY.sort()
# x_list, y_list = [list(l) for l in zip(*XY)]

# min_area = 10**24
# for i in range(N-K+1):
#     xs = x_list[i:i+K]
#     ys = y_list[i:i+K]
#     area = (xs[-1]-xs[0])*(max(ys)-min(ys))
#     min_area = min(
#         min_area,
#         area
#     )

# print(min_area)