S = input()

S_len = len(S)

cnt = 0
for i, s in enumerate(S):
    down, up = i, S_len-i-1
    if s == "D":
        cnt += down + 2*up
    elif s == "U":
        cnt += up + 2*down

print(cnt)