N, M, Q = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]
X = list(map(int, input().split()))
QUERY = [list(map(int, input().split())) for _ in range(Q)]

# O(QMN)
for l, r in QUERY:
    l, r = l-1, r-1 # 0-indexed 閉区間
    boxes = []
    for i, x in enumerate(X):
        if l <= i <= r:
            continue
        boxes.append(x)
    boxes.sort()
    is_used = [0]*N
    sum_num = 0
    for box in boxes:
        choosed = -1
        choosed_v = -1
        for i, (w, v) in enumerate(WV):
            if is_used[i]:
                continue
            if w <= box and v > choosed_v:
                choosed = i
                choosed_v = v
        if choosed == -1:
            continue
        is_used[choosed] = 1
        sum_num += choosed_v
    print(sum_num)
