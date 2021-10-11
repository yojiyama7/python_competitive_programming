from itertools import accumulate as acc

N = int(input())
A = [input().split('.') for _ in range(N)]

v_list = []
for a in A:
    if len(a) == 2:
        x, y = a
        v = int(x + f"{y:0<9}")
    else:
        v = int(a[0] + '0'*9)
    v_list.append(v)

t_list = []
f_list = []
for v in v_list:
    t = 0
    while v%2 == 0:
        t += 1
        v //= 2
    t_list.append(t)
    f = 0
    while v%5 == 0:
        f += 1
        v //= 5
    f_list.append(f)

# print(A)
# print(list(zip(t_list, f_list)))

self_valid = 0
tf_cnt = [[0 for _ in range(19)] for _ in range(19)]
for t, f in zip(t_list, f_list):
    if 2*t >= 18 and 2*f >= 18:
        self_valid += 1
    t = 18 if t > 18 else t
    f = 18 if f > 18 else f
    tf_cnt[t][f] += 1

tf_acc = [[0 for _ in range(20)] for _ in range(20)]
for i in range(19):
    for j in range(19):
        tf_acc[i+1][j+1] = tf_acc[i][j+1] + tf_acc[i+1][j] - tf_acc[i][j] + tf_cnt[i][j]

# print(*tf_cnt, sep='\n')
# print(*tf_acc, sep='\n')

ans = 0
for t, f in zip(t_list, f_list):
    y, x = max(0, 18-t), max(0, 18-f)
    score = tf_acc[19][19] - tf_acc[19][x] - tf_acc[y][19] + tf_acc[y][x]
    ans += score

ans -= self_valid
ans //= 2

print(ans)