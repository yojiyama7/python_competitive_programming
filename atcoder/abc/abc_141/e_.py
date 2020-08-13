N = int(input())
S = [ord(s) for s in input()]
# N = 5000
# S = "abcdefg" + "k"*4993

c = 0
for i in range(1, N):
    d = 0
    for s_j, t_j in zip(S, S[i:]):
        if s_j == t_j:
            d += 1
        else:
            c = max(c, min(d, i))
            d = 0
    c = max(c, min(d, i))

# print(S, t)
print(c)
