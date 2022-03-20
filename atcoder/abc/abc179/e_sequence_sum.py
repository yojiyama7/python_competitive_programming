# このタイプ苦手な問題
# なれてない

INF = 10**18

N, X, M = map(int, input().split())

idx_table = [-1]*M
table = [X]
for i in range(1, INF):
    a = table[-1]**2 % M
    table.append(a)
    if idx_table[a] == -1:
        idx_table[a] = i
    else:
        break

f = idx_table[table[-1]]
s = len(table)-1
w = s-f
# print(table)
# print((f, s), w)

ans = 0
for i, t in enumerate(table[:f]):
    ans += t
for i, t in enumerate(table[f:-1], start=f):
    ans += t * -(-(N-i)//w)

print(ans)

################################

# INF = 10**18

# N, X, M = map(int, input().split())

# table_idx = [-1]*M
# table = [X]
# for i in range(INF):
#     a = (table[i]**2) % M
#     table.append(a)
#     if table_idx[a] == -1:
#         table_idx[a] = i
#     else:
#         break

# print(table, len(table))

# ans = [0]*M
# loop_p = table_idx[table[-1]]
# for t in table[:loop_p]:
#     ans[t] += 1
# for i, t in enumerate(table[loop_p:], start=loop_p):
