N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

t = [to_num(t_i) for t_i in T]

def to_num(hand):
    return "rsp".find(hand)

# 0:あいこ, 1:勝ち, 2:負け
def check_result(m, e):
    return (e-m)%3

dp = [[0 for _ in range(3)] for _ in range(N+1)]
for i in range(1, K+1):
    for j in range(3):
        check_result(j, t[i-1])
        dp[i][j] = dp[i-1][]