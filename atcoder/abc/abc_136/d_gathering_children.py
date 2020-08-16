S = input()

n = len(S)
counts = [0]*n
r_start = 0
rl_point = None
for i in range(n):
    if S[i:i+2] == "RL":
        rl_point = i
    if S[i:i+2] in ["LR", "L"]:
        r = rl_point+1 - r_start
        l = i - rl_point
        # print(r, l)
        counts[rl_point] += (-(-r//2)) + l//2
        counts[rl_point+1] += r//2 + (-(-l//2))
        r_start = i+1

print(" ".join(map(str, counts)))

# RRRLLRRLL
