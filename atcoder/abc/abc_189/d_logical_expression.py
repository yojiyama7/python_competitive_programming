# 再帰的な遷移式を綺麗に立てれれば実装するだけになる

N = int(input())
S = [input() for _ in range(N)]

def solve(p):
    if p == 0:
        return (1)
    if S[p-1] == "AND":
        return solve(p-1)
    else:
        return solve(p-1) + 2**p

print(solve(N))
