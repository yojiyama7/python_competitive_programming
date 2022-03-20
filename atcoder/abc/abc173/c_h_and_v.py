from itertools import product, chain

H, W, K = map(int, input().split())
C = [input() for _ in range(H)]

sum_num = 0

for y in range(1<<H):
    for x in range(1<<W):
        s = [list(c) for c in C]
        for k in range(H):
            if (y>>k)%2:
                s[k] = ["X"]*W
        for k in range(W):
            if (x>>k)%2:
                for l in range(H):
                    s[l][k] = "X"
        black = sum(c=="#" for c in chain(*s))
        if black == K:
            sum_num += 1

print(sum_num)