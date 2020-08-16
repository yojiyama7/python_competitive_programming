# 20200704
from itertools import accumulate as acc

R, C, K = map(int, input().split())
S = [input() for _ in range(R)]
# R, C, K = 500, 500, 100
# S = [" "*C for _ in range(R)]

h, w = R, C

figure_size = 2*K-1
figure_size_half = K-1

S_acc = [[0]+list(acc(s_i=="x" for s_i in s)) for s in S]

count = 0
for ty in range(h-figure_size+1):
    for tx in range(w-figure_size+1):
        flag = True
        for dy in range(figure_size):
            y = ty+dy
            xl, xr = tx+abs(figure_size_half-dy), tx+figure_size-abs(figure_size_half-dy)
            # print(y, (xl, xr))
            if (S_acc[y][xr] - S_acc[y][xl]) > 0:
                flag = False
                break
        # print(flag)
        if flag:
            count += 1

print(count)

########################################

# 判定が複雑な探索は、判定を簡易化しておく
# あらかじめで計算しておいて、それを参照して判定

################################
#-------------------------------
################################

# R, C, K = map(int, input().split(" "))
# S = [input().replace("x", "1").replace("o", "0") for _ in range(R)]

# T = ["."*C for _ in range(R)]
# for std_y in range(R):
#     for std_x in range(C):
#         if S[std_y][std_x] != "x":
#             continue
#         if std_x-K+1 < 0 or std_y-K+1 < 0:
#             continue 
#         for y in range(K*2-1):
#             start = abs(y-(K-1))
#             size = 2*(K-start-1) + 1
#             # print(" "*start + "*"*size + " "*start)
#         S[std_y-K+1+y][std_x-K+1+start:std_x-K+1+start+size]

################################

# # TLE

# R, C, K = map(int, input().split(" "))
# S = [input().replace("o", "0").replace("x", "1") for _ in range(R)]

# # 開始、サイズを y から算出 する
# def is_diamond_white(std_pos):
#     std_x, std_y = std_pos
#     for y in range(K*2-1):
#         start = abs(y-(K-1))
#         size = 2*(K-start-1) + 1
#         # print(" "*start + "*"*size + " "*start)
#         s = S[std_y+y][std_x+start:std_x+start+size]
#         if int(s):
#             return False
#     return True

# count = 0
# for y in range(max(0, R-(2*K-1)+1)):
#     for x in range(max(0, C-(2*K-1)+1)):
#         count += is_diamond_white((x, y))
#         # if is_diamond_white((x, y)):
#         #     print("---", x, y)
#         #     for line in S[y:y+2*K-1]:
#         #         print(line[x:x+2*K-1])

# print(count)

# pos = x, y = (2, 0)
# for line in S[y:y+2*K-1]:
#     print(line[x:x+2*K-1])
# print(is_diamond_white(pos))