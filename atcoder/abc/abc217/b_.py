S = [input() for _ in range(3)]

all_set = {"ABC", "ARC", "AGC", "AHC"}
ans = list(all_set - set(S))[0]
print(ans)