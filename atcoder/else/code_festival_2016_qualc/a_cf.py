INF = 10**18

S = input()

first_C = INF
for i, s in enumerate(S):
    if s == 'C':
        first_C = i
        break

last_F = -INF
for i in range(len(S)-1, -1, -1):
    if S[i] == 'F':
        last_F = i
        break

if first_C < last_F:
    print("Yes")
else:
    print("No")