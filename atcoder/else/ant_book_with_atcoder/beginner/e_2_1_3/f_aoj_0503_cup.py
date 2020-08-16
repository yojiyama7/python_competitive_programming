# パズル: グラフ
# 操作: 辺
# 状態: ノード

from collections import deque

def rindex(l, a):
    for i, x in enumerate(l[::-1]):
        if x == a:
            return len(l)-i-1
    return -1

def move(t_l, a, b):
    s = 0
    for i, x in enumerate(t_l):
        if i == a:
            x = b
        s += 3**i * x
    return s

while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    S = [list(map(int, input().split()))[1:] for _ in range(3)]

    l = [-1]*N
    for i, s in enumerate(S):
        for s_j in s:
            s_j = s_j-1
            l[s_j] = i
    start = sum(3**i*l_i for i, l_i in enumerate(l))

    possible = [False]*(3**N)
    possible[start] = True
    q = deque([start])
    while q:
        t = q.popleft()
        t_l = [0]*N
        i = 0
        while t > 0:
            t_l[i] = t%3
            t //= 3
            i += 1
        m = [-1]*3
        for i in range(3):
            m[i] = rindex(t_l, i)
        if m[0] > m[1]:
            p = move(t_l, m[0], 1)
            if possible[p]:
                continue
            possible[p] = True
            q.append(p)
        elif m[1] >= 0:
            p = move(t_l, m[1], 0)
            if possible[p]:
                continue
            possible[p] = True
            q.append(p)
        if m[1] > m[2]:
            p = move(t_l, m[1], 2)
            if possible[p]:
                continue
            possible[p] = True
            q.append(p)
        elif m[2] >= 0:
            p = move(t_l, m[2], 1)
            if possible[p]:
                continue
            possible[p] = True
            q.append(p)
    if True in [possible[0], possible[3**N-1]]:
        print()
        

        