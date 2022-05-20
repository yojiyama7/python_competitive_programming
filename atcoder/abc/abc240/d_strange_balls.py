N = int(input())
A = list(map(int, input().split()))

q = []
q_cnt_sum = 0
for a in A:
    if not q:
        q.append([a, 1])
        q_cnt_sum += 1
        print(q_cnt_sum)
        continue
    # print(q)
    top = q[-1]
    if top[0] == a:
        q[-1][1] += 1
        q_cnt_sum += 1
        if top[0] == top[1]:
            q_cnt_sum -= top[1]
            q.pop()
    else:
        q.append([a, 1])
        q_cnt_sum += 1
    print(q_cnt_sum)
