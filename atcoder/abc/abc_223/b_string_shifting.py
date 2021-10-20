S = input()

S_len = len(S)

l = [S[i:] + S[:i] for i in range(S_len)]
l.sort()

print(l[0])
print(l[-1])