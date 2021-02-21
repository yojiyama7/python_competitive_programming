def char_calc_add(s, v):
    x = ord(s)
    x -= ord('a')
    x += v
    x %= 26
    x += ord('a')
    return chr(x)

S = input()
K = int(input())

S_len = len(S)

t = list(S)
for i, s in enumerate(S):
    # これ↓
    if s == 'a':
        continue
    x = ord(s)-ord('a')
    cost = 26-x
    if cost <= K:
        K -= cost
        t[i] = 'a'
if K:
    t[-1] = char_calc_add(t[-1], K)

print("".join(t))
