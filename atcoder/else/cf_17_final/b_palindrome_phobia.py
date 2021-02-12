from collections import Counter

S = input()

S_counter = Counter(S)
if max([abs(S_counter[a] - S_counter[b]) for a, b in zip("abc", "bca")]) <= 1:
    print("YES")
else:
    print("NO")