N = int(input())
Q = int(input())
Q = [list(map(int, input().split())) for _ in range(Q)]

ln = list(range(N))
rn = list(range(N))

is_reverse = 0

for q in Q:
    q_id = q[0]
    if 1 <= q_id <= 2:
        a, b = [arg-1 for arg in q[1:]]
        if is_reverse ^ (q_id-1):
            rn[a], rn[b] = rn[b], rn[a]
        else:
            ln[a], ln[b] = ln[b], ln[a]
    elif q_id == 3:
        is_reverse = not is_reverse
    else:
        a, b = [arg-1 for arg in q[1:]]
        if is_reverse:
            print(N*ln[b]+rn[a])
        else:
            print(N*ln[a]+rn[b])
    # print(*q, ln, rn)
