from collections import Counter

S = input()

if len(S) == 1:
    print("Yes" if S == "8" else "No")
    exit()
elif len(S) == 2:
    print("Yes" if int(S)%8 == 0 or int(S[::-1])%8 == 0 else "No")
    exit()

S_counter = Counter(S)

for i in range(1000):
    if i%8:
        continue
    t = f"{i:0>3}"
    t_counter = Counter(t)
    if t_counter["0"]:
        continue
    if all(S_counter[c] >= t_counter[c] for c in "123456789"):
        print("Yes")
        exit()

print("No")
