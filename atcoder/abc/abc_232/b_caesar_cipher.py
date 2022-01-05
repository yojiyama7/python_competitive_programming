S = input()
T = input()

Sl = [ord(s)-ord('a') for s in S]
Tl = [ord(t)-ord('a') for t in T]

diff = [(sl-tl)%26 for sl, tl in zip(Sl, Tl)]
if len(set(diff)) == 1:
    print("Yes")
else:
    print("No")
