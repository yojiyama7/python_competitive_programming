N, M = list(map(int, input().split()))
PS = [input().split() for _ in range(M)]

ps = [(int(p)-1, s) for p, s in PS]

ac = [0]*N
wa = [0]*N
for p, s in ps:
    if s == "AC":
        ac[p] = 1
    else:
        if ac[p] == 0:
            wa[p] += 1

print(sum(ac), sum([a*w for a, w in zip(ac, wa)]))