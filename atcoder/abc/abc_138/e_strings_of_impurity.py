from bisect import bisect_right

S = input()
T = input()

s_len = len(S)

indexs_by_char = dict([s, []] for s in (S))
for i, s in enumerate(S):
    indexs_by_char[s].append(i)
# print(indexs_by_char)
indexs_len = dict([[k, len(v)] for k, v in indexs_by_char.items()])
# print(indexs_len)

s_count = 0
current_i = -1
for t in T:
    if t not in indexs_by_char:
        print(-1)
        exit()
    j = None
    while True:
        j = bisect_right(indexs_by_char[t], current_i)
        if j < indexs_len[t]:
            break
        s_count += 1
        current_i = -1
    current_i = indexs_by_char[t][j]

print(s_len*s_count + current_i+1)
