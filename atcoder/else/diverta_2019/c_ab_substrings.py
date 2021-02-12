N = int(input())
S = [input() for _ in range(N)]

bz = 0
za = 0
ba = 0
cnt = 0
for s in S:
    if s[0] == "B" and s[-1] == "A":
        ba += 1
    elif s[0] == "B":
        bz += 1
    elif s[-1] == "A":
        za += 1
    cnt += sum(s[j:j+2] == "AB" for j in range(len(s)-1))

cnt += max(0, ba-1)
if ba and bz:
    bz -= 1
    cnt += 1
if ba and za:
    za -= 1
    cnt += 1
cnt += min(za, bz)

print(cnt)
