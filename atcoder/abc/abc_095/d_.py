# かけらも見えんが
# 円弧系は覚える必要がありそう

N, C = map(int, input().split())
XV = [list(map(int, input().split())) for _ in range(N)]

# X, V = zip(*XV)
lf, ls, rf, rs = [[0]]*4
for x, v in enumerate(XV):
    lf.append(lf[-1] + (v - (C-x)*2))
    ls.append(ls[-1] + (v - (C-x)))
    rf.append(rf[-1] + (v - x*2))
    rs.append(rs[-1] + (v - x))



