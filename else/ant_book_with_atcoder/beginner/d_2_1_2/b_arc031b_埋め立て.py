# ARC 031 B 埋め立て
# https://atcoder.jp/contests/arc031/tasks/arc031_2

from copy import deepcopy
from itertools import chain

A = [list(input()) for _ in range(10)]

def dfs(map_data, pos):
    x, y = pos
    if not (0 <= x < 10 and 0 <= y < 10) or map_data[y][x] == "x":
        return False
    map_data[y][x] = "x"
    dfs(map_data, (x+1, y))
    dfs(map_data, (x-1, y))
    dfs(map_data, (x, y+1))
    dfs(map_data, (x, y-1))

for y in range(10):
    for x in range(10):
        if A[y][x] == "o":
            continue
        m = deepcopy(A)
        m[y][x] = "o"
        dfs(m, (x, y))
        if "o" in list(chain(*m)):
            continue
        print("YES")
        exit()
print("NO")
