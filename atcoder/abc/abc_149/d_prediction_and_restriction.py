# K個の独立した問題として考える

N, K = map(int, input().split())
RSP = list(map(int, input().split()))
T = input()

def is_win(me, other):
    if me == 0 and other == 1:
        return True
    elif me == 1 and other == 2:
        return True
    elif me == 2 and other == 0:
        return True
    return False

def char_to_num(s):
    if s == "r":
        return 0
    elif s == "s":
        return 1
    else:
        return 2

# dp[i][j] = i回目のじゃんけんでjを出して取れる最大の点数([i%K]ごとに独立)
dp = [[-1 for j in range(3)] for i in range(N+1)]
dp[0] = [0, 0, 0]
for i in range(1, N+1):
    t = char_to_num(T[i-1])
    if i <= K:
        for j in range(3):
            dp[i][j] = is_win(j, t)*RSP[j]
    else:    
        for j in range(3):
            dp[i][j] = max(
                [dp[i-K][k] + is_win(j, t)*RSP[j] for k in range(3) if j != k]
            )

# print(dp)

r = sum(map(max, dp[-K:]))
print(r)
################################

# NOT AC

# N, K = map(int, input().split())
# RSP = list(map(int, input().split()))
# T = input()

# t = [to_num(t_i) for t_i in T]

# def to_num(hand):
#     return "rsp".find(hand)

# # 0:あいこ, 1:勝ち, 2:負け
# def check_result(m, e):
#     return (e-m)%3

# dp = [[0 for _ in range(3)] for _ in range(N+1)]
# for i in range(1, K+1):
#     for j in range(3):
#         p = check_result(j, t[i-1])
#         dp[i][j] = max(dp[i-1]) + RSP[j]*(p==1)

# for i in range(K+1, N+1):
#     for j in range(3):
#         p = check_result(j, t[i-1])
#         RSP[]*(p==1)
#         dp[i][j] = 