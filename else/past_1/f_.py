S = input()

b = 0
c = 0
t = []
for i, s in enumerate(S):
    if str.isupper(s):
        c += 1
    if c == 2:
        t.append(S[b:i+1])
        b = i+1
        c = 0

x = "".join(sorted(t, key=lambda x: str.lower(x)))
print(x)