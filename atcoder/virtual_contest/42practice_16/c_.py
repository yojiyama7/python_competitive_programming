from itertools import groupby

S = input()

print("".join(c + str(len(list(g))) for c, g in groupby(S)))
