# WAAAAAAAAA
# gg

N = int(input())
S = input()

l = 0
r = N-1

p = [-1]*N
for i, s in enumerate(S):
    if s == "L":
        p[i] = l+1
        l += 2
    if s == "R":
        p[i] = r+1
        r -= 2
    if l > r:
        l = 1
        r = N-2

for p_i in p:
    print(p_i)

# 1_3___2