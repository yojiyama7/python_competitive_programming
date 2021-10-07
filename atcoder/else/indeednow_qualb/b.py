INF = 10**18

S = input()
T = input()

def solve():
    if len(S) != len(T):
        return -1
    ans = INF
    for i in range(len(S)):
        if S == T[i:] + T[:i]:
            ans = min(ans, i)
    if ans == INF:
        return -1
    return ans

print(solve())
