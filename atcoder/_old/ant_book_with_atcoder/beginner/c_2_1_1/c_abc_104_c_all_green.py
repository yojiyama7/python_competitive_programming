# ABC 104 C - All Green
# https://atcoder.jp/contests/abc104/tasks/abc104_c

# no miss gg
# ちょい 特殊 bit 全探索

D, G = map(int, input().split())
PC = [list(map(int, input().split())) for _ in range(D)]

p, c = zip(*PC)

min_count = 10**18
for i in range(1<<D):
    h = -1
    point = 0
    count = 0
    for j in range(D):
        if (i>>j)%2:
            point += 100*(j+1)*p[j] + c[j]
            count += p[j]
        else:
            h = j
    if h > -1 and G > point:
        x = -(-(G-point)//(100*(h+1)))
        if x > p[h]:
            continue
        count += x
    min_count = min(min_count, count)

print(min_count)

