S = input()

S_len = len(S)

l = set()
i = 0
while i < S_len:
    if S[i] == '@':
        i += 1
        t = ""
        while i < S_len and 'a' <= S[i] <= 'z':
            t += S[i]
            i += 1
        if t:
            l.add(t)
    else:
        i += 1

ans = sorted(l)
print(*ans, sep='\n')
