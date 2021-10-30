from itertools import chain
from collections import Counter

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]

c = Counter(chain(*AB))
many_egdes_cnt = sum(v > 1 for v in c.values())
if many_egdes_cnt == 1:
    print("Yes")
else:
    print("No")

################################

# N = int(input())
# AB = [list(map(int, input().split())) for _ in range(N-1)]

# a0, b0 = AB[0]
# if all(a0 in ab for ab in AB) or all(b0 in ab for ab in AB):
#     print("Yes")
# else:
#     print("No")
