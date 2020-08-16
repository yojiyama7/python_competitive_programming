N, Q = map(int, input().split())
FTX = [list(map(int, input().split())) for _ in range(Q)]

# 各コンテナがどのコンテナの上にあるか
root = [-1]*N
# 各机の一番上のコンテナ
top = list(range(N))

for f, t, x in FTX:
    f, t, x = f-1, t-1, x-1
    # 机f から 机t に コンテナx より上を移動する
    ord_top_f = top[f]
    top[f] = root[x]
    root[x] = top[t]
    top[t] = ord_top_f

    # print(root, top)

# 各コンテナがどの机の上にあるか
where = list(range(N))
for i, c in enumerate(top):
    while c != -1:
        where[c] = i
        c = root[c]

for where_i in where:
    print(where_i+1)


