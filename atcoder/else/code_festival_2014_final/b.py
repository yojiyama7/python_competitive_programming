S = list(map(int, input()))

a = S[0]
for i, s in enumerate(S[1:]):
    if i%2 == 0:
        a -= s
    else:
        a += s

print(a)