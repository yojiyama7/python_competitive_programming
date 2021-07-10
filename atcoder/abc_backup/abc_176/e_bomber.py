from bisect import bisect_left, bisect_right

H, W, M = map(int, input().split())
YX = [list(map(int, input().split())) for _ in range(M)]
# H, W, M = 3*10**5, 3*10**5, 3*10**5
# YX = [[(i*100)//W, (i*100)%W] for i in range(M)]

X_sets = [[] for _ in range(W+1)]
Y_sets = [[] for _ in range(H+1)]
for y, x in YX:
    X_sets[x].append(y)
    Y_sets[y].append(x)

[s.sort() for s in X_sets]
[s.sort() for s in Y_sets]

# print(X_sets, Y_sets)

X_set_max_len = max(map(len, X_sets))
Y_set_max_len = max(map(len, Y_sets))

# print("ppp", X_set_max_len, Y_set_max_len)

# for s in X_sets:
#     print(s)

X_list = set(i for i, s in enumerate(X_sets) if len(s) == X_set_max_len)
Y_list = set(i for i, s in enumerate(Y_sets) if len(s) == Y_set_max_len)

score = X_set_max_len + Y_set_max_len - 1
# print("b", score, X_list, Y_list)
for x in X_list:
    for y in Y_list:
        c = bisect_right(X_sets[x], y) - bisect_left(X_sets[x], y)
        # print(x, y, c)
        if c == 0:
            score += 1
            print(score)
            exit()

print(score)